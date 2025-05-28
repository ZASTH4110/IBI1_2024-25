import xml.dom.minidom
import xml.sax
import time

# DOM Implementation 
def analyze_with_dom(file_path):
    start = time.time()  # Start timing

    # Load and parse the entire XML tree into memory
    dom_tree = xml.dom.minidom.parse(file_path)
    collection = dom_tree.documentElement
    terms = collection.getElementsByTagName("term")  # Get all <term> elements

    # Dictionary to store the term(s) with the most <is_a> children for each namespace
    max_is_a = {
        "molecular_function": [[], 0],
        "biological_process": [[], 0],
        "cellular_component": [[], 0]
    }

    # Traverse all <term> nodes
    for term in terms:
        namespace = term.getElementsByTagName("namespace")[0].firstChild.data
        term_id = term.getElementsByTagName("id")[0].firstChild.data
        is_a_count = len(term.getElementsByTagName("is_a"))  # Count <is_a> children

        # Update max count and store the corresponding term id(s)
        if namespace in max_is_a:
            if is_a_count > max_is_a[namespace][1]:
                max_is_a[namespace] = [[term_id], is_a_count]
            elif is_a_count == max_is_a[namespace][1]:
                max_is_a[namespace][0].append(term_id)

    end = time.time()
    return max_is_a, end - start  # Return result and execution time


#SAX Handler Class
class GosaxHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_tag = ""       # Current tag being processed
        self.namespace = ""         # <namespace> content
        self.term_id = ""           # <id> content
        self.is_a_count = 0         # Number of <is_a> elements in a <term>

        # Dictionary to track max <is_a> counts per namespace
        self.max_is_a = {
            "molecular_function": [[], 0],
            "biological_process": [[], 0],
            "cellular_component": [[], 0]
        }

    def startElement(self, tag, attrs):
        self.current_tag = tag
        if tag == "term":
            # Reset values for new term
            self.namespace = ""
            self.term_id = ""
            self.is_a_count = 0
        elif tag == "is_a":
            self.is_a_count += 1

    def characters(self, content):
        # Accumulate text content from <id> and <namespace> tags
        if self.current_tag == "namespace":
            self.namespace += content.strip()
        elif self.current_tag == "id":
            self.term_id += content.strip()

    def endElement(self, tag):
        if tag == "term":
            # When a <term> ends, check if it has the max number of <is_a>
            if self.namespace in self.max_is_a:
                if self.is_a_count > self.max_is_a[self.namespace][1]:
                    self.max_is_a[self.namespace] = [[self.term_id], self.is_a_count]
                elif self.is_a_count == self.max_is_a[self.namespace][1]:
                    self.max_is_a[self.namespace][0].append(self.term_id)
        self.current_tag = ""  # Reset tag


#SAX Parsing Function
def analyze_with_sax(file_path):
    handler = GosaxHandler()
    start = time.time()  # Start timing

    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)  # Disable namespace processing
    parser.setContentHandler(handler)
    parser.parse(file_path)

    end = time.time()
    return handler.max_is_a, end - start



file = "C:/Users/ziten/IBI1_2024-25/Practical 14/go_obo.xml"
# Run DOM parser
print("Analyzing with DOM...")
dom_result, dom_time = analyze_with_dom(file)
print("\nDOM Results:")
for k, v in dom_result.items():
    print(f"{k}: {v[0]} with {v[1]} is_a elements")
print(f"DOM parsing took {dom_time:.4f} seconds")
# Run SAX parser
print("\nAnalyzing with SAX...")
sax_result, sax_time = analyze_with_sax(file)
print("\nSAX Results:")
for k, v in sax_result.items():
    print(f"{k}: {v[0]} with {v[1]} is_a elements")
print(f"SAX parsing took {sax_time:.4f} seconds")

# SAX ran faster than DOM

