from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
            def do_GET(self):
             self.send_response(200)
             self.send_header('Content-type', 'text/html')
             self.send_header('Set-Cookie', 'cookie_name=value; SameSite=None; Secure') 
             self.end_headers()  




        content = """


                        <header>
                <nav>
                    <h2 class="title">colorsense</h2>
                        <ul>
                            <li class="home">HOME</li>
                            <li class="about">ABOUT</li>
                            <li class="account">ACCOUNT</li>
                            <li class="contact">CONTACT</li>
                        </ul>
                    <div id="menuButton" onclick="menuLateral()">&#9776;</div>
                        <section class="menu-lateral">
                                <p class="home">HOME</p>
                                <p class="about">ABOUT</p>
                                <p class="account">ACCOUNT</p>
                                <p class="contact">CONTACT</p>
                        </section>
                </nav>
            </header>
            <script>
                function menuLateral() {
                    const menu = document.querySelector('section.menu-lateral')
                    const buttonMenu = document.querySelector('div#menuButton')
                    buttonMenu.classList.toggle('open')
                    menu.classList.toggle("opened")
                }
            </script>




            <div class="area-circle">
                <section class="circle">  </section>
            </div>

            <div class="texts">
            <p class="text-1">Lorem ipsum dolor sit amet consectetur. 
                Gravida at ac hac. Quisque in risus 
                ornare porttitor. At venenatis</p>
                <p class="text-3"><span class="strong" style="font-weight: 900;">how use colorsense?</span> <br>
                select your image above 
                or point your camera</p>
            <p class="text-2">Lorem ipsum dolor sit amet consectetur. 
                Gravida at ac hac. Quisque in risus 
                ornare porttitor. At venenatis</p>
            </div>
            <h1 class="changes">Changes in lives</h1>


            <footer>
                <p>&copy; 2023 My Website. All rights reserved.</p>
            </footer>
        """


        html = f"""
        <html>
            <head>
                <style>
                    .area-circle {{
    width: 100%;
    display: flex;
    justify-content: center;
  }}
  .circle {{
    width: 500px;
    height: 500px;
    border-radius: 50%;
    background-color: #E5D9D9;
    box-sizing: border-box;
    border: 30px solid #F2C43B;
  }}
  body {{
      background-color: #f5f4ea;
      margin: 0;
      padding: 0;
      font-family: sans-serif;
  }}
  *{{
    transition: 300ms;
  }}
  header {{
      margin: 0;
      padding: 2%;
  }}
  nav {{
      display: flex;
  }}
  ul {{
      display: flex;
      width: 43%;
      justify-content: center;
      margin-top: 7px;
      margin-left: 20%;
      padding: 0;
  }}
  li {{
      margin-left: 50px;
      list-style: none;
      padding: 0;
  }}
  .title {{
      padding: 0;
      margin: 0;
  }}
  .contact, .about, .account, .home {{
      margin: 10px;
      width: 90%;
      background-color:transparent;
      text-align: center  ;
      padding: 10px;
      border-radius: 10px;
      padding: 10px 100px 10px 10px;
      color: rgb(129, 129, 129);
      }}
  #menuButton {{
      display: none;
      position: fixed;
      top: 10px;
      right: 15px;
      font-size: 30px;
      color: #000000;
      transition: right 0.3s ease-in-out;
  }}
  #menuButton.open {{
      top: 10px;
      right: 250px;
  }}
  .menu-lateral {{
      position: fixed;
      top: 0;
      right: -300px;
      background-color: rgba(14, 14, 14, 0.932);
      z-index: 1;
      height: 100%;
      padding: 20px;
      transition: right 0.2s ease-in-out;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.267);
  }}
  .menu-lateral.opened {{
      right: 0;
      transition: right 0.2s ease-in-out;
  }}
  .text-1 {{
    position: fixed;
    left: 100px;
    top: 150px;
    width: 200px;
  }}
  .text-2 {{
    position: fixed;
    right: 100px;
    top: 200px;
    width: 200px;
  }}
  .text-3 {{
    position: fixed;
    bottom: 50px;
    right: 45%;
    padding-bottom: 100px;
  }}
  .changes {{
    position: fixed;
    bottom: 200px;
    right: 10%;
    font-size: 50px;
    width: 300px;
  }}

  
  @media only screen and (max-width: 1000px) {{
    .text-1 {{
    position: fixed;
    left: 20px;
    top: 200px;
    width: 130px;
  }}
  .text-2 {{
    position: fixed;
    right: 20px;
    top: 250px;
    width: 130px;
  }}
  .text-3 {{
    position: fixed;
    bottom: 50px;
    right: 45%;
  }}
  .changes {{
    bottom: 100px;
    right: 50px;
  }}
}}
  @media only screen and (max-height: 700px) {{
    .text-3 {{
      position: fixed;
      bottom: 50px;
      left: 20px;
    }}
    .changes {{
      bottom: 40px;
    }}
    .circle {{
      width: 430px;
      height: 430px;
    }}
  }}
   @media only screen and (max-height: 560px) {{
    .text-1 {{
      position:initial;
      margin: 20px;
      font-size: 12px;
      width: 80%;
      
    }}
    .text-2 {{
      position:initial;
      margin: 20px;
      font-size: 12px;
      width: 80%;
    }}
    .text-3 {{
      position:initial;
      margin: 20px;
      font-size: 12px;
      width: 80%;
    }}
    .circle{{
          width: 300px;
          height: 300px;
          border: 20px solid #F2C43B;
        }}
        .texts{{
          display: block;
        }}
  }}
  @media only screen and (max-width: 800px) {{
      ul {{
          display: none;
      }}
      nav {{
          display: flex;
          justify-content: center;
          margin-bottom: 10%;
      }}
      #menuButton{{
          display: flex;
      }}
      .circle{{
        width: 380px;
        height: 380px;
        border: 20px solid #F2C43B;
      }}
      .changes {{
        top: 50px;
        left: 10px;
        font-size: 30px;
      }}

  }}
  @media only screen and (max-width: 600px) {{
    .text-1 {{
    position:initial;
    margin: 5px;
    
  }}
  .text-2 {{
    position:initial;
    margin: 5px;
    
  }}
  .text-3 {{
    position:initial;
    width: 100px;
    margin: 5px;
  
  }}
  .texts {{
    display: flex;
    justify-content: space-around;
    width: 100%;
  }}
  .circle {{
    margin-bottom: 50px;
  }}
  .changes {{
    top: 50px;
    left: 10px;
    font-size: 30px;
  }}
  }}
  @media only screen and (max-width: 400px) {{
    .text-1 {{
    position:initial;
    margin: 20px;
    font-size: 12px;
    width: 80%;
    
  }}
  .text-2 {{
    position:initial;
    margin: 20px;
    font-size: 12px;
    width: 80%;
  }}
  .text-3 {{
    position:initial;
    margin: 20px;
    font-size: 12px;
    width: 80%;
  }}
  .circle{{
        width: 300px;
        height: 300px;
        border: 20px solid #F2C43B;
      }}
  .changes {{
    bottom: 390px;
    left: 50px;
    font-size: 20px;
  }}
  .texts {{
    display: block;
    text-align: right;

  }}
  }}

  footer {{
    display: flex;
    margin-top: 200px;
    justify-content: center;
    border-top: 2px solid rgba(0, 0, 0, 0.397);
    width: 96%;
    margin-left: 2%;
  }}






          
                </style>
                
            </head>

            <body>
                {content}    
            </body>

        </html>
        """





        self.wfile.write(html.encode('utf-8'))

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Server running at http://localhost:8000")
    httpd.serve_forever()

if __name__ == '__main__':
    run()