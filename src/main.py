from textnode import TextNode, TextType

def main():
    dummy_text_node = TextNode("Hello, World!", TextType.LINK, "https://example.com")
    print(dummy_text_node.__repr__())

main()