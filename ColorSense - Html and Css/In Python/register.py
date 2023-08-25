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


                    <main>
                        <section class="area-login">
                            <h1 class="register">Register</h1>
                            <input type="text" placeholder="Username" class="username"><br>
                            <input type="password" placeholder="Password" class="pass"><br>
                            <input type="password" placeholder="Confirm the password" class="pass2"><br>
                        <button>register</button>
                        </section>
                    </main>            


                <footer>
                    <p>&copy; 2023 My Website. All rights reserved.</p>
                </footer>

        """



        html = f"""
        <html>
            <head>
                <style>
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
        background-color: rgba(0, 0, 0, 0.671);
        height: 100%;
        padding: 20px;
        transition: right 0.2s ease-in-out;
        box-shadow: 0 0 15px rgba(0, 0, 0, 0.781);
    }}
.menu-lateral.opened {{
        right: 0;
        transition: right 0.2s ease-in-out;
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
    }}













    .area-login{{
        width: 80%;
        display: block;
        text-align: center;      
        margin-left: 10%;
    }}   




    .register {{
      
        font-size: 50px;
        text-align: left;
        margin-left: 25%;
        text-shadow: 2px 2px 2px rgba(128, 128, 128, 0.842);
    }}

    .username{{
        color: rgba(128, 128, 128, 0.842);
        width: 50%;
        padding: 30px 0px 20px  0px;
        border: none;
        font-size: larger;
        border-bottom: 2px solid rgba(0, 0, 0, 0.616);
        text-shadow: 2px 2px 2px rgba(128, 128, 128, 0.603);
        background-color: #f5f4ea;
        outline: none;
    }}

    .pass{{
        color: rgba(128, 128, 128, 0.842);
        width: 50%;
        padding: 30px 0px 20px  0px;
        border: none;
        font-size: larger;
        border-bottom: 2px solid rgba(0, 0, 0, 0.616);
        text-shadow: 2px 2px 2px rgba(128, 128, 128, 0.603);
        background-color: #f5f4ea;
        outline: none;
    }}

    .pass2{{
        color: rgba(128, 128, 128, 0.842);
        width: 50%;
        padding: 30px 0px 20px  0px;
        border: none;
        font-size: larger;
        border-bottom: 2px solid rgba(0, 0, 0, 0.616);
        text-shadow: 2px 2px 2px rgba(128, 128, 128, 0.603);
        background-color: #f5f4ea;
        outline: none;
    }}

    .pass:focus, .pass2:focus, .username:focus{{
        border-bottom: 2px solid  #F3C53C;
        border-top: none;
        border-left: none;                          
        border-right: none;
    }}
    ::placeholder{{
        color: #00000075;
        text-shadow: none;          
        font-weight: 100;  
        font-size: 18px;

    }}


    button{{
        background-color: #F3C53C;
        border: none;
        width: 30%;
        padding: 10px;
        margin-top: 30px;
        text-align: center;
        font-size: 30px;
        box-shadow: 3px 3px 3px rgba(128, 128, 128, 0.842);
    }}



    @media only screen and (max-width: 700px) {{
        .username, .pass, .pass2,  button {{
            width: 90%;                            
        }}
        .register{{
            margin-left: 5%;
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