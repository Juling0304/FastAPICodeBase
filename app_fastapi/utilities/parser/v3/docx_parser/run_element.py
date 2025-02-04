from typing import Any, cast

from lxml.etree import _Element


DOCX_XML_NAMESPACE_WORD = "w"
DOCX_XML_TEXT_TAG = "t"
DOCX_XML_PARAGRAPH_TAG = "p"
DOCX_XML_RUN_TAG = "r"
DOCX_XML_RPR_TAG = "rPr"
DOCX_XML_FOOTNOTE_REFERENCE_TAG = "footnoteReference"
DOCX_XML_ENDNOTE_REFERENCE_TAG = "endnoteReference"

DOCX_XML_NAMESPACES = {
    DOCX_XML_NAMESPACE_WORD: "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
}


class RunElement:
    def __init__(self, run_element: _Element, index: int) -> None:
        self._run_element = run_element
        self._index = index
        self._depth_from_paragraph_element = 0
        self._ancestor_paragraph_element = None
        self._child_text_element = None
        self._run_properties = None

        self._initialize_run_element()

    def _initialize_run_element(self) -> None:
        self._find_ancestor_paragraph_element()
        self._find_child_text_element_and_run_properties()

    def _find_ancestor_paragraph_element(self) -> None:
        ancestor_element: _Element | None = self._run_element
        while (ancestor_element.tag.split("}")[-1] != DOCX_XML_PARAGRAPH_TAG) and (
            ancestor_element != None
        ):
            ancestor_element: _Element = cast(
                _Element | None, ancestor_element.getparent()
            )
            self._depth_from_paragraph_element += 1
        else:
            self._ancestor_paragraph_element = ancestor_element

    def _find_child_text_element_and_run_properties(self) -> None:
        for child_element in self._run_element.iterchildren():
            child_element: _Element
            # 네임스페이스 뒤에 있는 태그 타입을 가져오기 위해 {namespace}type 구성에서 }를 선택하여 분할한다.
            child_tag: str = child_element.tag.split("}")[-1]

            if child_tag == DOCX_XML_RPR_TAG:
                if self._run_properties == None:
                    self._run_properties = {
                        DOCX_XML_FOOTNOTE_REFERENCE_TAG: False,
                        DOCX_XML_ENDNOTE_REFERENCE_TAG: False,
                    }
                for descendant_element in child_element.iterdescendants():
                    descendant_element: _Element
                    descendant_tag: str = descendant_element.tag.split("}")[-1]
                    descendant_attributes = {}
                    for attribute_name_with_namespace in descendant_element.attrib:
                        attribute_name = attribute_name_with_namespace.split("}")[-1]
                        descendant_attributes[attribute_name] = (
                            descendant_element.attrib[attribute_name_with_namespace]
                        )

                    self._run_properties[descendant_tag] = descendant_attributes

            elif child_tag == DOCX_XML_ENDNOTE_REFERENCE_TAG:
                if self._run_properties == None:
                    self._run_properties = {
                        DOCX_XML_FOOTNOTE_REFERENCE_TAG: False,
                        DOCX_XML_ENDNOTE_REFERENCE_TAG: False,
                    }
                self._run_properties[DOCX_XML_ENDNOTE_REFERENCE_TAG] = True

            elif child_tag == DOCX_XML_FOOTNOTE_REFERENCE_TAG:
                if self._run_properties == None:
                    self._run_properties = {
                        DOCX_XML_FOOTNOTE_REFERENCE_TAG: False,
                        DOCX_XML_ENDNOTE_REFERENCE_TAG: False,
                    }
                self._run_properties[DOCX_XML_FOOTNOTE_REFERENCE_TAG] = True

            elif child_tag == DOCX_XML_TEXT_TAG:
                self._child_text_element = child_element

    @property
    def run_element(self) -> _Element:
        return self._run_element

    @property
    def index(self) -> int:
        return self._index

    @property
    def depth_from_paragraph_element(self) -> _Element:
        return self._depth_from_paragraph_element

    @property
    def ancestor_paragraph_element(self) -> _Element:
        return self._ancestor_paragraph_element

    @property
    def child_text_element(self) -> _Element | None:
        return self._child_text_element

    @property
    def child_text(self) -> str:
        # t 엘리먼트가 None이 아닐 때, 엘리먼트 내부 텍스트가 공백이라면, text 속성값은 None으로 반환된다.
        if self._child_text_element != None and self._child_text_element.text != None:
            return self._child_text_element.text
        else:
            return ""

    @property
    def run_properties(self) -> dict[str, dict[str, Any]] | None:
        return self._run_properties
