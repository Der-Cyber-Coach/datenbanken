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
                # Die XML-Response schöner formatieren
                xml_data = minidom.parseString(response.text)
                pretty_xml = xml_data.toprettyxml()

                with open('pretty_response.xml', 'w', encoding='utf-8') as pretty_xml_file:
                    pretty_xml_file.write(pretty_xml)

                print('Schön formatierte Response wurde in pretty_response.xml gespeichert.')
            else:
                print('Fehler beim Senden des Requests. Status-Code:', response.status_code)
        except Exception as e:
            print('Fehler beim Senden des Requests:', str(e))

# Beispielverwendung der XmlRequestHandler-Klasse
if __name__ == "__main__":
    # URL mit dem angegebenen Request und dem richtigen Encoding
    url = f"https://www.fivb.org/vis2009/XmlRequest.asmx?Request=<Request Type='GetBeachMatchList' Fields='NoInTournament LocalDate LocalTime TeamAName TeamBName Court MatchPointsA MatchPointsB PointsTeamASet1 PointsTeamBSet1 PointsTeamASet2 PointsTeamBSet2 PointsTeamASet3 PointsTeamBSet3 DurationSet1 DurationSet2 DurationSet3'><Filter /> <!-- optional: contains the filter to use --> </Request>"

    request_handler = XmlRequestHandler(url)
    request_handler.send_request()
