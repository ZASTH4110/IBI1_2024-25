import xml.dom.minidom
import xml.sax
import time

# DOM IMPLEMENTATION
def analyze_with_dom(file_path):
    start = time.time()

    dom_tree = xml.dom.minidom.parse(file_path)
    collection = dom_tree.documentElement
    terms = collection.getElementsByTagName("term")

    max_is_a = {
    "molecular_function": [[], 0],
    "biological_process": [[], 0],
    "cellular_component": [[], 0]
    }


    for term in terms:
        namespace = term.getElementsByTagName("namespace")[0].firstChild.data
        term_id = term.getElementsByTagName("id")[0].firstChild.data
        is_a_count = len(term.getElementsByTagName("is_a"))

        if namespace in max_is_a:
            if is_a_count > max_is_a[namespace][1]:
                max_is_a[namespace] = [[term_id], is_a_count]
            elif is_a_count == max_is_a[namespace][1]:
                max_is_a[namespace][0].append(term_id)


    end = time.time()
    return max_is_a, end - start

# ------------------------------
# SAX IMPLEMENTATION
# ------------------------------
class GOSAXHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_tag = ""
        self.namespace = ""
        self.term_id = ""
        self.is_a_count = 0
        self.max_is_a = {
            "molecular_function": [[], 0],
            "biological_process": [[], 0],
            "cellular_component": [[], 0]
        }

    def startElement(self, tag, attrs):
        self.current_tag = tag
        if tag == "term":
            self.namespace = ""
            self.term_id = ""
            self.is_a_count = 0

        elif tag == "is_a":
            self.is_a_count += 1

    def characters(self, content):
        if self.current_tag == "namespace":
            self.namespace += content.strip()
        elif self.current_tag == "id":
            self.term_id += content.strip()

    def endElement(self, tag):
        if tag == "term":
            if self.namespace in self.max_is_a:
                if self.is_a_count > self.max_is_a[self.namespace][1]:
                    self.max_is_a[self.namespace] = [[self.term_id], self.is_a_count]
                elif self.is_a_count == self.max_is_a[self.namespace][1]:
                    self.max_is_a[self.namespace][0].append(self.term_id)

        self.current_tag = ""


def analyze_with_sax(file_path):
    handler = GOSAXHandler()
    start = time.time()
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    parser.setContentHandler(handler)
    parser.parse(file_path)
    end = time.time()
    return handler.max_is_a, end - start


file = "go_obo.xml"

print("Analyzing with DOM...")
dom_result, dom_time = analyze_with_dom(file)
print("\nDOM Results:")
for k, v in dom_result.items():
    print(f"{k}: {v[0]} with {v[1]} is_a elements")
print(f"DOM parsing took {dom_time:.4f} seconds")
print("\nAnalyzing with SAX...")
sax_result, sax_time = analyze_with_sax(file)
print("\nSAX Results:")
for k, v in sax_result.items():
    print(f"{k}: {v[0]} with {v[1]} is_a elements")
print(f"SAX parsing took {sax_time:.4f} seconds")

# Comment comparison
if dom_time < sax_time:
    print("\n# DOM ran faster in this test")
else:
    print("\n# SAX ran faster in this test")
