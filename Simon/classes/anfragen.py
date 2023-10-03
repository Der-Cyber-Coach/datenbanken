import requests
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

class XmlRequestHandler:
    def __init__(self, url):
        self.url = url

    def send_request(self):
        try:
            # Senden des HTTP-GET-Requests
            response = requests.get(self.url)

            # Überprüfen, ob die Anfrage erfolgreich war (Status-Code 200)
            if response.status_code == 200:
                # XML-Datei erstellen und den Wurzelknoten festlegen
                root = ET.Element('response')

                # Hinzufügen des Response-Texts als XML-Element
                response_element = ET.SubElement(root, 'data')
                response_element.text = response.text

                # Erstellen Sie ein ElementTree-Objekt aus dem Wurzelknoten
                tree = ET.ElementTree(root)

                # XML-Datei speichern
                with open('response.xml', 'wb') as xml_file:
                    tree.write(xml_file, encoding='utf-8')

                # Die XML-Response schöner formatieren
                xml_data = minidom.parseString(response.text)
                pretty_xml = xml_data.toprettyxml()

                with open('pretty_response.xml', 'w', encoding='utf-8') as pretty_xml_file:
                    pretty_xml_file.write(pretty_xml)

                print('Response wurde in response.xml gespeichert.')
                print('Schön formatierte Response wurde in pretty_response.xml gespeichert.')
            else:
                print('Fehler beim Senden des Requests. Status-Code:', response.status_code)
        except Exception as e:
            print('Fehler beim Senden des Requests:', str(e))

# Beispielverwendung der XmlRequestHandler-Klasse
if __name__ == "__main__":
    url = 'https://www.fivb.org/vis2009/XmlRequest.asmx?Request=%3CRequests%3E%3CRequest%20Type=%27GetBeachMatch%27%20No=%2715592%27%20Fields=%27NoInTournament%20LocalDate%20LocalTime%20TeamAType%20TeamAName%20TeamBType%20TeamBName%20Court%20MatchPointsA%20MatchPointsB%20PointsTeamASet1%20PointsTeamBSet1%20PointsTeamASet2%20PointsTeamBSet2%20PointsTeamASet3%20PointsTeamBSet3%20DurationSet1%20DurationSet2%20DurationSet3%27/%3E%3C/Requests%3E'
    request_handler = XmlRequestHandler(url)
    request_handler.send_request()
