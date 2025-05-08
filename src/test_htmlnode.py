import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        props = {
            "href": "https://www.wikipedia.org",
            "target": "_blank",
        }
        node = HTMLNode("<p>", "This is an HTML node", props)
        expected_repr = "HTMLNode(tag=<p>, value=This is an HTML node, props={'href': 'https://www.wikipedia.org', 'target': '_blank'}, children=None)"
        self.assertEqual(repr(node), expected_repr)

    def test_repr_with_children(self):
        props = {
            "href": "https://www.wikipedia.org",
            "target": "_blank",
        }
        children = [
            HTMLNode("<span>", "This is a child node", None),
            HTMLNode("<a>", "This is another child node", None)
        ]
        node = HTMLNode("<p>", None, props, children)
        expected_repr = "HTMLNode(tag=<p>, value=None, props={'href': 'https://www.wikipedia.org', 'target': '_blank'}, children=[HTMLNode(tag=<span>, value=This is a child node, props=None, children=None), HTMLNode(tag=<a>, value=This is another child node, props=None, children=None)])"
        self.assertEqual(repr(node), expected_repr)

    def test_props_to_html(self):
        props = {
            "href": "https://www.wikipedia.org",
            "target": "_blank",
        }
        node = HTMLNode("<p>", "This is an HTML node", props)
        expected_props_html = ' href="https://www.wikipedia.org" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_props_html)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"class": "weblink",  "href": "https://www.example.com"})
        self.assertEqual(node.to_html(), '<a class="weblink" href="https://www.example.com">Click me!</a>')

if __name__ == "__main__":
    unittest.main()