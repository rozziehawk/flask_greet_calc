from flask import Flask, request
#from flask import Flask, request
app = Flask(__name__)


@app.route("/")
def display_home_page():
    html = """
        <html>
        <body>
            <h1>Greet Home Page</h1>
            <p>Lorem ipsum dolor sit amet, duo no sanctus scriptorem, no vim debet consulatu conceptam. Cu vel fabellas indoctum. Ne saepe aeterno impedit vis. Usu esse commune et. Quo ea oratio tamquam gubergren, nec erat interesset omittantur te.</p>

            <p>Quo mutat assentior cu, te iudico facete pri. Congue percipitur definitionem vix eu, sea in affert appellantur, hinc erat viderer nam ad. Nec zril hendrerit abhorreant no, augue nostrud hendrerit ut vix, paulo labitur oporteat an ius. Indoctum cotidieque te cum, graece repudiare at ius.</p>

            <p>His diceret electram et. Atqui causae vim id. Id eligendi gloriatur eos, alterum delicata ei qui, ut per elitr possim. Aliquam laboramus no usu, ut mea luptatum maluisset.</p>

            <p>Et erat aperiri sea, verterem adversarium eu nam, eam probo omnes graeco ea. Vero mentitum dissentiunt nam te, porro maluisset et mei. Ex vis utinam intellegat, ne nec liber aeque officiis. Ea nominati voluptaria definitionem nec, alii phaedrum eu mel. Ei his altera recusabo quaestio, cum at harum aliquid perfecto.</p>

            <p>Odio denique deterruisset nec ad, denique molestie quo ad, minimum abhorreant ut duo. Tibique appellantur an his, eum at solet luptatum. Ea congue delicata intellegebat quo. Hinc nihil eu mei, at pro inani soluta.</p>
      
        </body>
        </html>        
        """
    return html

@app.route("/welcome")
def welcome():
#     """ show form for adding a comment"""
    return """Welcome!"""

@app.route("/welcome/home")
def welcome_home():
    """welcome/home, welcome/back, etc"""
    return """welcome home"""

@app.route("/welcome/back")
def welcome_back():
    """welcome/home, welcome/back, etc"""
    return """welcome back"""
   
    
    