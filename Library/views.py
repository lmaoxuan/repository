from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>HOMEPAGE</title>
        <link href="data:image/x-icon;base64,AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADb1FgAx8H/ANvU/wD/9/8A//f/AP/
        3/wD/9/8A//f/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADb1FgAx8H/ANvU/wYPD/8GDw//Bg8P/wYPD/8GDw//AP/3/wD/9/8AAAAAAAA
        AAAAAAAAAAAAAAAAAAADb1FgAx8H/ANvU/wYPD/8GDw//Bg8P/wYPD/8rAP//KwD//wYPD/8A//f/AP/3/wAAAAAAAAAAAAAAAAAAAAAA29RYAMf
        B/wDb1P8GDw//Bg8P/wYPD/8GDw//Bg8P/ysA//8GDw//AP/3/wD/9/8AAAAAAAAAAAAAAAAA29RYAMfB/wDb1P8A//f/Bg8P/wYPD/8GDw//Bg8
        P/wYPD/8GDw//Bg8P/wD/9/8A//f/AP/3/wAAAAAAAAAAANvUWADHwf8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AP/
        3/wD/9/8AAAAAAAAAAADb1FgAx8H/ANvU/wD/9/8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AAAAAAAAAAAA29RYAMf
        B/wDb1P8A//f/AP/3/wYPD/8GDw//AP/3/wD/9/8A//f/Bg8P/wYPD/8A//f/AP/3/wAAAAAAAAAAANvUWADHwf8A//f/AP/3/wYPD//////////
        //wYPD/8A//f/Bg8P////////////Bg8P/wD/9/8AAAAAAAAAAAAAAAAA29RYAMfB/wD/9/8GDw///////wYPD/8GDw//AP/3/wYPD///////Bg8
        P/wYPD/8AAAAAAAAAAAAAAAAAAAAAANvUWADHwf8A29T/AP/3/wYPD/8GDw//AP/3/wD/9/8A//f/Bg8P/wYPD/8A//f/AAAAAAAAAAAAAAAAAAA
        AAAAAAAAA29RYAMfB/wDb1P8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADb1FgAx8H/ANv
        U/wD/9/8A//f/AP/3/wD/9/8A//f/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAA//8AAP//AADwHwAA4A8AAMAHAADABwAAgAMAAIADAACAAwAAgAMAAIADAADABwAAwAcAAOAPAADwHwAA//8
        AAA==" rel="icon" type="image/x-icon" />
    <style>
    body {background-color: black;}
    h1 {
        color: orange;
        font-family: comic sans ms;
        font-size: 300%;
    }

    h2 {
        color: orange;
        font-family: comic sans ms;
        font-size: 260%
    }

    h3 {
        color: orange;
        font-family: comic sans ms;
        font-size: 220%
    }

    h4 {
        font-family: comic sans ms;
        color: teal;
        font-size: 180%
    }

    p {
      font-family: comic sans ms;
      font-size: 65%;
      color: white;
    }

    a {
        color: green;
        font-family: comic sans ms;
        font-size: 100%;
    }

    </style>
    </head>
    <body>

    <h1>HOMEPAGE<h1>
    <h2>HOME<h2>
    <br><br><a href="/catalog/">GO TO CATALOG</a><br><br><br>
    <a href="/aoxuan/">see the author</a><br><br><br>
    
    <p style='font size: 45%'>
    Whenever I am feeling low<br>
    I look around me and I know<br>
    There's a place that will stay within me<br>
    Wherever I may choose to go<br>
    I will always recall the city<br>
    Know every street and shore<br>
    Sail down that river which brings us life<br>
    Winding through my Singapore<br><br>
    This is home, truly<br>
    Where I know I must be<br>
    Where my dreams wait for me<br>
    Where that river always flows<br>
    This is home, surely<br>
    As my senses tell me<br>
    This is where I won't be alone<br>
    For this is where I know it's home.<br><br>
    When there are troubles to go through<br>
    I look around and start anew<br>
    For there's comfort in the knowledge<br>
    That home's about its people too<br>
    So we'll build our dreams together<br>
    Just like we've done before<br>
    Just like that river which brings us life<br>
    There'll always be Singapore<br><br>
    This is home, truly<br>
    Where I know I must be<br>
    Where my dreams wait for me<br>
    Where that river always flows<br>
    This is home, surely<br>
    As my senses tell me<br>
    This is where I won't be alone<br>
    For this is where I know it's home.<br><br>
    This is home, truly<br>
    Where I know I must be<br>
    This is where I won't be alone<br>
    For this is where I know I'm home.<br>
    </p>
    
    <p><br></p>
    
    <footer style="font-size:90%; color:yellow ">created by lim ao xuan</footer>
    </body>
    </html> 
    ''')


def catalog(request):
    return HttpResponse('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>CATALOG</title>
        <link href="data:image/x-icon;base64,AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADb1FgAx8H/ANvU/wD/9/8A//f/AP/
        3/wD/9/8A//f/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADb1FgAx8H/ANvU/wYPD/8GDw//Bg8P/wYPD/8GDw//AP/3/wD/9/8AAAAAAAA
        AAAAAAAAAAAAAAAAAAADb1FgAx8H/ANvU/wYPD/8GDw//Bg8P/wYPD/8rAP//KwD//wYPD/8A//f/AP/3/wAAAAAAAAAAAAAAAAAAAAAA29RYAMf
        B/wDb1P8GDw//Bg8P/wYPD/8GDw//Bg8P/ysA//8GDw//AP/3/wD/9/8AAAAAAAAAAAAAAAAA29RYAMfB/wDb1P8A//f/Bg8P/wYPD/8GDw//Bg8
        P/wYPD/8GDw//Bg8P/wD/9/8A//f/AP/3/wAAAAAAAAAAANvUWADHwf8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AP/
        3/wD/9/8AAAAAAAAAAADb1FgAx8H/ANvU/wD/9/8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AAAAAAAAAAAA29RYAMf
        B/wDb1P8A//f/AP/3/wYPD/8GDw//AP/3/wD/9/8A//f/Bg8P/wYPD/8A//f/AP/3/wAAAAAAAAAAANvUWADHwf8A//f/AP/3/wYPD//////////
        //wYPD/8A//f/Bg8P////////////Bg8P/wD/9/8AAAAAAAAAAAAAAAAA29RYAMfB/wD/9/8GDw///////wYPD/8GDw//AP/3/wYPD///////Bg8
        P/wYPD/8AAAAAAAAAAAAAAAAAAAAAANvUWADHwf8A29T/AP/3/wYPD/8GDw//AP/3/wD/9/8A//f/Bg8P/wYPD/8A//f/AAAAAAAAAAAAAAAAAAA
        AAAAAAAAA29RYAMfB/wDb1P8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADb1FgAx8H/ANv
        U/wD/9/8A//f/AP/3/wD/9/8A//f/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAA//8AAP//AADwHwAA4A8AAMAHAADABwAAgAMAAIADAACAAwAAgAMAAIADAADABwAAwAcAAOAPAADwHwAA//8
        AAA==" rel="icon" type="image/x-icon" />
    <style>
    body {background-color: black;}
    h1 {
        color: orange;
        font-family: comic sans ms;
        font-size: 300%;
    }

    h2 {
        color: orange;
        font-family: comic sans ms;
        font-size: 260%
    }

    h3 {
        color: orange;
        font-family: comic sans ms;
        font-size: 220%
    }

    h4 {
        font-family: comic sans ms;
        color: teal;
        font-size: 180%
    }

    p {
      font-family: comic sans ms;
      font-size: 140%;
      color: white;
    }

    a {
        color: green;
        font-family: comic sans ms;
        font-size: 200%;
    }

    </style>
    </head>
    <body>
    
    <h1>CATALOG OF STUFF<h1>
    <h2>ALL THE GOOD STUFF</h2>
    <a style="font size:250%", href="/aoxuan/">THE AUTHOR</a><br><br>
    
    <h2>LINKS BELOW</h2>
    
    <a href="/grammarly/">GRAMMARLY<br><br></a> <a href="/grammarly"><img 
    src="https://i.ibb.co/w0qsMXD/grammarlyicon.png" alt="grammarlyicon" border="0"></a><br /><a target='_blank' 
    href='https://imgbb.com/'></a><br><br>
    
    <a href="/youtube/">YOUTUBE<br></a>
    <a href="/youtube/"><img src="https://i.ibb.co/987kmQY/yt-icon.jpg" width="290" height="275" alt="" border="0"></a><br><br>
    
    <a href="/tetris/">TETRIS<br><br></a>
    <a href="/tetris"><img src="https://i.ibb.co/26HG21m/Screenshot-2022-06-06-at-9-51-53-PM.png" width="290" height="269"
    alt="" border="0"></a><br/>
    
    <br><br><br><br><br><br><br><br><a href="/home/">BACK TO HOME</a>
    
    <p><br></p>
    <footer style="font-size:150%; color:yellow ">created by lim ao xuan</footer>
    
    </body>
    </html>
    ''')


def grammarly(request):
    return HttpResponse('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Grammarly</title>
        <link href="data:image/x-icon;base64,AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADb1FgAx8H/ANvU/wD/9/8A//f/AP/
        3/wD/9/8A//f/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADb1FgAx8H/ANvU/wYPD/8GDw//Bg8P/wYPD/8GDw//AP/3/wD/9/8AAAAAAAA
        AAAAAAAAAAAAAAAAAAADb1FgAx8H/ANvU/wYPD/8GDw//Bg8P/wYPD/8rAP//KwD//wYPD/8A//f/AP/3/wAAAAAAAAAAAAAAAAAAAAAA29RYAMf
        B/wDb1P8GDw//Bg8P/wYPD/8GDw//Bg8P/ysA//8GDw//AP/3/wD/9/8AAAAAAAAAAAAAAAAA29RYAMfB/wDb1P8A//f/Bg8P/wYPD/8GDw//Bg8
        P/wYPD/8GDw//Bg8P/wD/9/8A//f/AP/3/wAAAAAAAAAAANvUWADHwf8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AP/
        3/wD/9/8AAAAAAAAAAADb1FgAx8H/ANvU/wD/9/8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AAAAAAAAAAAA29RYAMf
        B/wDb1P8A//f/AP/3/wYPD/8GDw//AP/3/wD/9/8A//f/Bg8P/wYPD/8A//f/AP/3/wAAAAAAAAAAANvUWADHwf8A//f/AP/3/wYPD//////////
        //wYPD/8A//f/Bg8P////////////Bg8P/wD/9/8AAAAAAAAAAAAAAAAA29RYAMfB/wD/9/8GDw///////wYPD/8GDw//AP/3/wYPD///////Bg8
        P/wYPD/8AAAAAAAAAAAAAAAAAAAAAANvUWADHwf8A29T/AP/3/wYPD/8GDw//AP/3/wD/9/8A//f/Bg8P/wYPD/8A//f/AAAAAAAAAAAAAAAAAAA
        AAAAAAAAA29RYAMfB/wDb1P8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADb1FgAx8H/ANv
        U/wD/9/8A//f/AP/3/wD/9/8A//f/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAA//8AAP//AADwHwAA4A8AAMAHAADABwAAgAMAAIADAACAAwAAgAMAAIADAADABwAAwAcAAOAPAADwHwAA//8
        AAA==" rel="icon" type="image/x-icon" />
    <style>
    body {background-color: black;}
    h1 {
        color: orange;
        font-family: comic sans ms;
        font-size: 300%;
    }
    
    h2 {
        color: orange;
        font-family: comic sans ms;
        font-size: 260%
    }
    
    h3 {
        color: orange;
        font-family: comic sans ms;
        font-size: 220%
    }
    
    h4 {
        font-family: comic sans ms;
        color: teal;
        font-size: 180%
    }
    
    p {
      font-family: comic sans ms;
      font-size: 140%;
      color: white;
    }
    
    a {
        color: green;
        font-family: comic sans ms;
        font-size: 200%;
    }
    
    </style>
    </head>
    <body>

    
    <h1>this is not a title for this page</h1> 
    <p>i love comic sans<br>comic sans best<br>comic sans forever</p>
    <a href="https://www.grammarly.com/">GRAMMARLY</a>
    <p> </p>
    <a href="https://imgbb.com/"><img src="https://i.ibb.co/vH09z4z/ppp.png" alt="" border="0"></a>
    <p><br> <br></p>
    <header><h2>This is an advertisement for Grammarly</h2></header>
    
    
    <section><h4>Writing's not easy</h3></section>    
    <p>That's why Grammarly can help. This sentence is grammatically correct, but it's wordy, and hard to read. 
    <br>It undermines the writer's message and the word choice is bland. <br>Grammarly's cutting edge technology 
    helps you craft compelling, understandable writing that makes an impact on your reader. <br>Much better. Are you 
    ready to give it a try? Installation is simple and free. Visit Grammarly.com today!</p> 
    <p> </p>
    
    <section><h4>This is Tyler.</h4></section>
    <p>Tyler, with Grammarly’s help, is writing an email to his boss, Anita.<br>
    Tyler sits just 15 feet away, though it can feel like the distance to Antarctica, approximately 47 million feet.<br>
    Tyler desperately wants Anita to like him, but doesn’t want to sound unsure of himself.<br>
    He also wants to explain the incident at the elevator.<br>
    But this probably isn’t the email for that.<br>
    It’s an email asking to lead a team workshop, because more collaboration would be really helpful. . . beneficial.<br>
    But Tyler worries that Anita doesn’t think he’s competent. Especially after the time he told her: “I’m a suppository of information”<br>
    And she gave him this look:<br>
    Since he clearly didn’t know what a suppository was.<br>
    This time, Tyler is determined to find the right words, the ones that will connect best with Anita.<br>
    So that when Tyler sends his email, he receives a response in just 4 minutes and 12 seconds that includes phrases like: “I’m impressed!” and “Such initiative!”<br>
    And the distance between Tyler and Anita stops feeling so far.<br>
    Grammarly – Helping you connect.<br>
    Go to grammarly.com to download.</p>
    <p> </p>
    
    <section><h4>Grammarly does more than catch errors.</h4></section>
    <p>With Grammarly, you can find really good-- no, perfect words that make <br>
    your writing sharp, or explicit, or excellent-- distinctive! As a matter of fact, for what it's worth,<br> 
    Grammarly can... yeah, that's long... we can get rid of that, and this-- good, and this! Or how about this: <br>
    Grammarly helps you be concise. If your tone might make someone feel like this (guy gets thrown into Antarctica), <br>
    Grammarly can remind you. It would help if you softened your tone. And if you need the support, Grammarly <br>
    encourages you to write confidently. Because the better we all communicate, the better we connect. Grammarly, <br>
    helping you connect. Go to grammarly.com and download today. </p>
    
    <br><br><br><br><br><br><br><br><br><br><br><br>
    <a style='color:fuchsia' href="/catalog">Back to catalog</a><br>
    <a style='color:fuchsia' href="/home">Back to home</a>
    
    <p><br></p>
    
    <footer style="font-size:150%; color:yellow ">created by lim ao xuan</footer>
    </body>
    </html>''')


def youtube(request):
    return HttpResponse('''
    <!DOCTYPE html>
    <html>
    <head>
       <title>YOUTUBE</title>
       <link href="data:image/x-icon;base64,AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADb1FgAx8H/ANvU/wD/9/8A//f/AP/
        3/wD/9/8A//f/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADb1FgAx8H/ANvU/wYPD/8GDw//Bg8P/wYPD/8GDw//AP/3/wD/9/8AAAAAAAA
        AAAAAAAAAAAAAAAAAAADb1FgAx8H/ANvU/wYPD/8GDw//Bg8P/wYPD/8rAP//KwD//wYPD/8A//f/AP/3/wAAAAAAAAAAAAAAAAAAAAAA29RYAMf
        B/wDb1P8GDw//Bg8P/wYPD/8GDw//Bg8P/ysA//8GDw//AP/3/wD/9/8AAAAAAAAAAAAAAAAA29RYAMfB/wDb1P8A//f/Bg8P/wYPD/8GDw//Bg8
        P/wYPD/8GDw//Bg8P/wD/9/8A//f/AP/3/wAAAAAAAAAAANvUWADHwf8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AP/
        3/wD/9/8AAAAAAAAAAADb1FgAx8H/ANvU/wD/9/8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AAAAAAAAAAAA29RYAMf
        B/wDb1P8A//f/AP/3/wYPD/8GDw//AP/3/wD/9/8A//f/Bg8P/wYPD/8A//f/AP/3/wAAAAAAAAAAANvUWADHwf8A//f/AP/3/wYPD//////////
        //wYPD/8A//f/Bg8P////////////Bg8P/wD/9/8AAAAAAAAAAAAAAAAA29RYAMfB/wD/9/8GDw///////wYPD/8GDw//AP/3/wYPD///////Bg8
        P/wYPD/8AAAAAAAAAAAAAAAAAAAAAANvUWADHwf8A29T/AP/3/wYPD/8GDw//AP/3/wD/9/8A//f/Bg8P/wYPD/8A//f/AAAAAAAAAAAAAAAAAAA
        AAAAAAAAA29RYAMfB/wDb1P8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADb1FgAx8H/ANv
        U/wD/9/8A//f/AP/3/wD/9/8A//f/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAA//8AAP//AADwHwAA4A8AAMAHAADABwAAgAMAAIADAACAAwAAgAMAAIADAADABwAAwAcAAOAPAADwHwAA//8
        AAA==" rel="icon" type="image/x-icon" />
    <style>
    body {background-color: black;}
    h1 {
       color: red;
       font-family: comic sans ms;
       font-size: 160%;
    }

    h2 {
       color: red;
       font-family: comic sans ms;
       font-size: 160%
    }

    h3 {
       color: red;
       font-family: comic sans ms;
       font-size: 150%
    }

    h4 {
       font-family: comic sans ms;
       color: yellow;
       font-size: 145%
    }

    p {
     font-family: comic sans ms;
     font-size: 125%;
     color: beige;
    }

    a {
       color: green;
       font-family: comic sans ms;
       font-size: 100%;
    }

    </style>
    </head>
    <body>
    
    <h3>this is twitch<h3>
    <h1>plot twist: its youtube<h1>
    <a href="https://www.youtube.com/">YOUTUBE</a><br><br><br><br>
    
    <header><h3>The Youtube Community</h3></header>
    <p style='color:violet'>"No one:<br>
    Not a single soul:<br>
    This video: exists<br>
    This comment: hold my beer<br>
    Me: so you have chosen death<br>
    Death: that's a big yikes from me dawg<br>
    Also death: I wasn't expecting special forces<br>
    Me: mom can we have death<br>
    Mom: we already have death at home<br>
    Death at home: surprised pikachu face<br>
    This video literally makes me cry every time<br>
    Who else is watching this in <current year>????<br>
    This video: wait that's illegal<br>
    Also this video: why do I hear boss music???"<br><br>
    -Youtube comments</p><br><br><br><br><br>
    
    <header><h3>Brief History of Youtube</h3></header><br>
    <h4>2005:</h4>
    <p>YouTube was founded by Chad Hurley, Steve Chen, and Jawed Karim, when they worked for PayPal.</p><br>
    <h4>2006:</h4>
    <p>During the summer of 2006, YouTube was one of the fastest growing sites on the World Wide Web, hosting more 
    than 65,000 new video uploads. The site delivered an average of 100 million video views per day in July. 
    On October 9, 2006, it was announced that the company would be purchased by Google for US$1.65 billion in stock.</p>
    <p><br></p>
    <h4>2007-2012:</h4>
    
    <p>It is estimated that in 2007, YouTube consumed as much bandwidth as the entire Internet in 2000.
    Youtube continued to grow and grow, slowly introducing new features, registering new domains, as the numbers of its
    users increased. In 2012 there was the first youtube video to reach one billion views.</p> <br>
    
    <h4>From then on:</h4>
    <p>
    2013<br>	March‒June – Transition to the "One" channel layout<br>
            September – Removal of video responses feature<br>
            September‒November – Google+ integration of comments sections<br>
    2014<br>	October – 60 fps videos<br>
    2015<br>	March – 360° videos<br>
            November – YouTube Red launches<br>
    2016<br>	February – YouTube subscription service<br>
            April – live streaming with 360° and 1440p<br>
    2017<br>	February – YouTube TV launches<br>
            March – Ability to modify video annotations removed<br>
            August – Logo changed and new "polymer" website version defaulted (preselected)<br>
            September – Video Editor discontinued<br>
    2018<br>	June – Introduction of "Premieres"<br>
    2019<br>	January – Removal of annotations and AutoShare features<br>
            September – Visible subscriber counts abbreviated to three leading digits<br>
    2020<br>	Removal of option for legacy website version ("disable_polymer")<br>
            Removal of legacy "Creator Studio"<br>
            August – Removal of optional email notifications for uploads<br>
    2021<br>	July  – Purge of pre-2017 unlisted videos through mass-privatization.<br>
            November – Removal of public dislikes count<br></p>
    
    <br><br><br><br><br><br><br><br><br><br><br><br>
    <a style='color:fuchsia' href="/catalog">Back to catalog</a><br>
    <a style='color:fuchsia' href="/home">Back to home</a>
    
    <p><br><br><br></p>
    <footer style="font-size:130%; color:yellow ">created by lim ao xuan</footer>
    </body>
    </html>
    ''')


def tetris(request):
    return HttpResponse('''
    <!DOCTYPE html>
    <html>
    <head>
       <title>Tetris</title>
       <link href="data:image/x-icon;base64,AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADb1FgAx8H/ANvU/wD/9/8A//f/AP/
        3/wD/9/8A//f/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADb1FgAx8H/ANvU/wYPD/8GDw//Bg8P/wYPD/8GDw//AP/3/wD/9/8AAAAAAAA
        AAAAAAAAAAAAAAAAAAADb1FgAx8H/ANvU/wYPD/8GDw//Bg8P/wYPD/8rAP//KwD//wYPD/8A//f/AP/3/wAAAAAAAAAAAAAAAAAAAAAA29RYAMf
        B/wDb1P8GDw//Bg8P/wYPD/8GDw//Bg8P/ysA//8GDw//AP/3/wD/9/8AAAAAAAAAAAAAAAAA29RYAMfB/wDb1P8A//f/Bg8P/wYPD/8GDw//Bg8
        P/wYPD/8GDw//Bg8P/wD/9/8A//f/AP/3/wAAAAAAAAAAANvUWADHwf8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AP/
        3/wD/9/8AAAAAAAAAAADb1FgAx8H/ANvU/wD/9/8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AAAAAAAAAAAA29RYAMf
        B/wDb1P8A//f/AP/3/wYPD/8GDw//AP/3/wD/9/8A//f/Bg8P/wYPD/8A//f/AP/3/wAAAAAAAAAAANvUWADHwf8A//f/AP/3/wYPD//////////
        //wYPD/8A//f/Bg8P////////////Bg8P/wD/9/8AAAAAAAAAAAAAAAAA29RYAMfB/wD/9/8GDw///////wYPD/8GDw//AP/3/wYPD///////Bg8
        P/wYPD/8AAAAAAAAAAAAAAAAAAAAAANvUWADHwf8A29T/AP/3/wYPD/8GDw//AP/3/wD/9/8A//f/Bg8P/wYPD/8A//f/AAAAAAAAAAAAAAAAAAA
        AAAAAAAAA29RYAMfB/wDb1P8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADb1FgAx8H/ANv
        U/wD/9/8A//f/AP/3/wD/9/8A//f/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAA//8AAP//AADwHwAA4A8AAMAHAADABwAAgAMAAIADAACAAwAAgAMAAIADAADABwAAwAcAAOAPAADwHwAA//8
        AAA==" rel="icon" type="image/x-icon" />
    <style>
    body {background-color: black;}
    h1 {
       color: orange;
       font-family: comic sans ms;
       font-size: 300%;
    }

    h2 {
       color: orange;
       font-family: comic sans ms;
       font-size: 260%
    }

    h3 {
       color: orange;
       font-family: comic sans ms;
       font-size: 220%
    }

    h4 {
       font-family: comic sans ms;
       color: teal;
       font-size: 180%
    }

    p {
     font-family: comic sans ms;
     font-size: 140%;
     color: white;
    }

    a {
       color: green;
       font-family: comic sans ms;
       font-size: 200%;
    }

    </style>
    </head>
    <body>
    
    <h1>TETRIS<h1>
    <h2>the stacking game</h2>
    <br><br>
    <h3>to play it:</h3>
    <a href="https://tetr.io/">TETR.IO</a><br>
    <a href="https://jstris.jezevec10.com/">JSTRIS</a>
    <br><br><br>
    <h3>to get good:</h3>
    <a href="/tetris/resources/">Resources and Setups</a>
    <br>
    <a href="/tetris/openers/">Practical Openers</a>
    
    <br><br><br><br><br><br><br><br><br><br><br><br>
    <a style='color:fuchsia' href="/catalog">Back to catalog</a><br>
    <a style='color:fuchsia' href="/home">Back to home</a>
    
    <p><br></p>
    <footer style="font-size:150%; color:yellow ">created by lim ao xuan</footer>
    </body>
    </html>
    ''')


def tetrisresources(request):
    return HttpResponse('''
    <!DOCTYPE html>
    <html>
    <head>
       <title>Resources</title>
       <link href="data:image/x-icon;base64,AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADb1FgAx8H/ANvU/wD/9/8A//f/AP/
        3/wD/9/8A//f/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADb1FgAx8H/ANvU/wYPD/8GDw//Bg8P/wYPD/8GDw//AP/3/wD/9/8AAAAAAAA
        AAAAAAAAAAAAAAAAAAADb1FgAx8H/ANvU/wYPD/8GDw//Bg8P/wYPD/8rAP//KwD//wYPD/8A//f/AP/3/wAAAAAAAAAAAAAAAAAAAAAA29RYAMf
        B/wDb1P8GDw//Bg8P/wYPD/8GDw//Bg8P/ysA//8GDw//AP/3/wD/9/8AAAAAAAAAAAAAAAAA29RYAMfB/wDb1P8A//f/Bg8P/wYPD/8GDw//Bg8
        P/wYPD/8GDw//Bg8P/wD/9/8A//f/AP/3/wAAAAAAAAAAANvUWADHwf8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AP/
        3/wD/9/8AAAAAAAAAAADb1FgAx8H/ANvU/wD/9/8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AAAAAAAAAAAA29RYAMf
        B/wDb1P8A//f/AP/3/wYPD/8GDw//AP/3/wD/9/8A//f/Bg8P/wYPD/8A//f/AP/3/wAAAAAAAAAAANvUWADHwf8A//f/AP/3/wYPD//////////
        //wYPD/8A//f/Bg8P////////////Bg8P/wD/9/8AAAAAAAAAAAAAAAAA29RYAMfB/wD/9/8GDw///////wYPD/8GDw//AP/3/wYPD///////Bg8
        P/wYPD/8AAAAAAAAAAAAAAAAAAAAAANvUWADHwf8A29T/AP/3/wYPD/8GDw//AP/3/wD/9/8A//f/Bg8P/wYPD/8A//f/AAAAAAAAAAAAAAAAAAA
        AAAAAAAAA29RYAMfB/wDb1P8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADb1FgAx8H/ANv
        U/wD/9/8A//f/AP/3/wD/9/8A//f/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAA//8AAP//AADwHwAA4A8AAMAHAADABwAAgAMAAIADAACAAwAAgAMAAIADAADABwAAwAcAAOAPAADwHwAA//8
        AAA==" rel="icon" type="image/x-icon" />
    <style>
    body {background-color: black;}
    h1 {
       color: orange;
       font-family: comic sans ms;
       font-size: 300%;
    }

    h2 {
       color: orange;
       font-family: comic sans ms;
       font-size: 260%
    }

    h3 {
       color: orange;
       font-family: comic sans ms;
       font-size: 220%
    }

    h4 {
       font-family: comic sans ms;
       color: teal;
       font-size: 180%
    }

    p {
     font-family: comic sans ms;
     font-size: 170%;
     color: white;
    }

    a {
       color: green;
       font-family: comic sans ms;
       font-size: 140%;
    }

    </style>
    </head>
    <body>
    
    <h1>RESOURCES FOR TETRIS<h1>
    <h2>(INCLUDES PC SETUPS)</h2><br>
    
    <p>Openers/ Midgame:</p>
    <a href="https://four.lol">FOUR.LOL</a><br><br>
    <p>Openers</p>
    <a href="https://harddrop.com/wiki/Tetris_Wiki">HARD DROP</a><br><br>
    <p>Videos</p>
    <a href="https://www.youtube.com/">YOUTUBE</a><br>
    <a href="/youtube">For more info regarding youtube</a><br><br>
    <p>Best chance fields for 1st-7th pc (2nd pc prioritises O and T)</p>
    <a href="https://knewjade.github.io/best-chance-field/">KNEWJADE'S BEST CHANCE FIELDS</a><br><br>
    <p>Setup Lookup Sheet</p>
    <a href="https://docs.google.com/spreadsheets/d/1xgAvuGQOI8zWO-87auNuFkHoldN_ZfZHH-eeEIO7r8Q/edit?usp=sharing">HSTERT'S SETUP LOOKUP SHEET</a><br><br>
    <p>2nd pc, saving S/Z and O</p>
    <a href="https://torchlight.github.io/tetnotes/second-pc.html">TORCHLIGHT 2ND PC --> DPC</a><br><br>
    <p>PC FINDER/ PRACTICE</p>
    <a href="https://wirelyre.github.io/tetra-tools/pc-solver.html">WEB-BASED PC FINDER</a><br><br>
    <p>GUIDE TO PCS</p>
    <a href="https://docs.google.com/document/d/1udtq235q2SdoFYwMZNu-GRYR-4dCYMkp0E8_Hw1XTyg/edit">PC THEORY</a><br><br>
    
    <br><br><br>
    <p style='font-size= 200%'>STUFF TO DO</p>
    <a href="/tetris">PLAY TETRIS</a>
    <br>
    <a href="/home">GO HOME</a>
    
    <p><br></p>
    <footer style="font-size:150%; color:yellow ">created by lim ao xuan</footer>
    </body>
    </html>
    ''')


def tetrisopeners(request):
    return HttpResponse('''
    <!DOCTYPE html>
    <html>
    <head>
       <title>Openers</title>
       <link href="data:image/x-icon;base64,AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADb1FgAx8H/ANvU/wD/9/8A//f/AP/
        3/wD/9/8A//f/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADb1FgAx8H/ANvU/wYPD/8GDw//Bg8P/wYPD/8GDw//AP/3/wD/9/8AAAAAAAA
        AAAAAAAAAAAAAAAAAAADb1FgAx8H/ANvU/wYPD/8GDw//Bg8P/wYPD/8rAP//KwD//wYPD/8A//f/AP/3/wAAAAAAAAAAAAAAAAAAAAAA29RYAMf
        B/wDb1P8GDw//Bg8P/wYPD/8GDw//Bg8P/ysA//8GDw//AP/3/wD/9/8AAAAAAAAAAAAAAAAA29RYAMfB/wDb1P8A//f/Bg8P/wYPD/8GDw//Bg8
        P/wYPD/8GDw//Bg8P/wD/9/8A//f/AP/3/wAAAAAAAAAAANvUWADHwf8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AP/
        3/wD/9/8AAAAAAAAAAADb1FgAx8H/ANvU/wD/9/8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AAAAAAAAAAAA29RYAMf
        B/wDb1P8A//f/AP/3/wYPD/8GDw//AP/3/wD/9/8A//f/Bg8P/wYPD/8A//f/AP/3/wAAAAAAAAAAANvUWADHwf8A//f/AP/3/wYPD//////////
        //wYPD/8A//f/Bg8P////////////Bg8P/wD/9/8AAAAAAAAAAAAAAAAA29RYAMfB/wD/9/8GDw///////wYPD/8GDw//AP/3/wYPD///////Bg8
        P/wYPD/8AAAAAAAAAAAAAAAAAAAAAANvUWADHwf8A29T/AP/3/wYPD/8GDw//AP/3/wD/9/8A//f/Bg8P/wYPD/8A//f/AAAAAAAAAAAAAAAAAAA
        AAAAAAAAA29RYAMfB/wDb1P8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADb1FgAx8H/ANv
        U/wD/9/8A//f/AP/3/wD/9/8A//f/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAA//8AAP//AADwHwAA4A8AAMAHAADABwAAgAMAAIADAACAAwAAgAMAAIADAADABwAAwAcAAOAPAADwHwAA//8
        AAA==" rel="icon" type="image/x-icon" />
    <style>
    body {background-color: black;}
    h1 {
       color: orange;
       font-family: comic sans ms;
       font-size: 300%;
    }

    h2 {
       color: orange;
       font-family: comic sans ms;
       font-size: 260%
    }

    h3 {
       color: orange;
       font-family: comic sans ms;
       font-size: 220%
    }

    h4 {
       font-family: comic sans ms;
       color: teal;
       font-size: 180%
    }

    p {
     font-family: comic sans ms;
     font-size: 140%;
     color: #ee82ee;
    }

    a {
       color: teal;
       font-family: comic sans ms;
       font-size: 180%;
       font-weight: bold;
    }

    </style>
    </head>
    <body>
    
    
    <h1>PRACTICAL TETRIS OPENERS (FOR BEGINNERS)<h1>
    <h2>from four.lol and hard drop</h2><br>
    <h3>(Click the links to learn more)</h3>
    
    <p style="font-size:170%">These openers are based on the assumption that these below functions are available:<br>

    7-Bag: every piece appears exactly once every 7 pieces<br>
    Hold : the player can store away pieces for later use (e.g. hold a T piece to make a T-Spin later on)<br>
    SRS kicks: if a rotation fails without offset, then the game tests a few other nearby locations; <br>
    kicks are required to make T-Spin Triples<br>
    multiple Previews: you can see which pieces will appear next<br>
    T-Spins are rewarded<br>
    Combos are rewarded<br>
    Perfect Clear (PC): reaching a completely empty playfield is rewarded<br></p>
    
    <br><br><h3>Early I piece</h3>
    <a href="https://four.lol/openers/tki">TKI 3 Opener</a><br>
    <a href="https://four.lol/openers/tki"><img src="https://i.ibb.co/L1Pznj4/tki.png" alt="tki" border="0"></a>
    <p>There are multiple variations of the TKI opener, all of them which require an early I and start off with an 
    opening T-spin double (TSD) that leads into more TSDs through LST stacking, freestyle TSDs, 
    or a perfect clear after 6 or 8 lines. The Flat Top/ Dingle continuation is most widely used for LST, while the others
    are more likely to have a 6-line PC.</p><br>
    <a href="https://harddrop.com/wiki/Ajanba_TSD">Ajanba TSD</a>
    <p>Invented by the player Ajanba, this resembles the TKI opener, but requires O before L/J. Continuations include
    mechanical TSDs, PC after 6, or 8 lines, or more T-spins, e.g. DSD or DMD -->10 or 14 line PC. There is also the
    mofumofu continuation.</p>
    
    <br><br><br><br><h3>Early L J pieces</h3>
    <a href="https://four.lol/openers/mko">MKO</a><br>
    <a href="https://four.lol/openers/mko"><img src="https://i.ibb.co/2kQMznx/mko.png" alt="mko" border="0"></a>
    <p>Requiring early L and J (the opener doesnt change when mirrored), a 6-piece setup is placed with T in hold 
    to perform a 4-line PC with 33% chance. Otherwise, more T-spins are done. The first TSD is done with an
    S/Z/T overhang, or an STMB cave. Then, one can build an 6-3, 7-2 or freestyle stack.</p><br>
    <a href="https://four.lol/methods/dt-cannon">DT Cannon</a><br>
    <a href="https://four.lol/methods/dt-cannon"><img src="https://i.ibb.co/jk8g1VV/dt-cannon.png" alt="dt-cannon" border="0"></a>
    <p>This opener is used with either early L and J, and allows the player to perform TSD-->TST, sending 
    12 lines in a combo. After this, there are multiple options to followup: S4W, a C-spin attack, shachiku train, 
    or a New DT. If one chooses to stack for tetrises, 9-0 stacking is easiest. Note that DT Cannon is a legit 
    t-spin setup that can also be built midgame.</p>
    
    <br><br><br><br><h3>Early Z T S pieces</h3>
    <a href="https://four.lol/perfect-clears/opener">PCO</a><br>
    <a href="https://four.lol/perfect-clears/opener"><img src="https://i.ibb.co/SrgqfP0/pco.png" alt="pco" border="0"></a>
    <p>An opener that can result in a pc with 84.64% chance if I is held, and a 61.19% chance to pc if I is not held
    i.e. placed down to make a 7-piece setup. There are a total of 63 solutions, and 53 non-strict minimal solutions.
    For vertically placed I there are 15 solutions needed for 61.19% pc chance. Horizontal I on first row has 8, 
    horizontal I on third row has 5, and there are 2 miscellaneous solutions (IILO and ILSO). Total there are 30 strict
    minimal solutions. This setup is easy to learn and solve, with its downside being its low PC rate. If a PC is not
    possible, there are continuations: C4W, PCO 4-5 stacking, etc.</p><br>
    <a href="https://four.lol/methods/bt-cannon">BT Cannon</a><br>
    <a href="https://four.lol/methods/bt-cannon"><img src="https://i.ibb.co/zSBGDrz/bt-cannon.png" alt="bt-cannon" border="0"></a>
    <p>BT cannon is a TSD-->TST setup. The BT Cannon Loop is a BT Cannon-->C-spin-->PC loop that needs 5 bags to execute.
    In 5 bags one will have 5 T pieces, and while the first T is used for setup the rest are all used for the T-spins,
    making this efficient in terms of attack. Note that BT cannon is a legit t-spin setup that can also be built 
    midgame.</p>
    
    <br><br><br><br><h3>Early O piece</h3>
    <a href="https://harddrop.com/wiki/Stickspin">Stickspin</a><br>
    <a href="https://harddrop.com/wiki/Stickspin"><img src="https://i.ibb.co/y4yYQ1p/stickspin.png" alt="stickspin" border="0"></a>
    <p>Stickspin is one of the most lethal openers in existence- in 3 bags, it does a TSS, TSD, and set ups a C-spin.
    Assuming B2B is maintained and the C-spin is done in a combo, 22 lines are sent. Stickspin is buildable when O
    comes before any of S, Z, or T, meaning there is a 87.5% to build stickspin from the first bag. From then on, build
    rates are 100%. There ae multiple T-spin continuations after the C-spin, adding extra lethality from the B2B
    already obtained. There are also some ways to stack for a 14-linePC after the C-spin, and the success rate is quite 
    high. There are also 8 or 10 line PCs that can be done while performing stickspin, however the chances are lower. 
    (33.73% and 10.79%-13.81% respectively) </p><br>
    <a href="https://four.lol/openers/hachispin">Hachispin</a><br>
    <a href="https://four.lol/openers/hachispin"><img src="https://i.ibb.co/KzDK8tr/hachispin.png" alt="hachispin" border="0"></a>
    <p>A TSS-->TST-->PC opener. The PC is done after 8 lines, meaning that one can do DPC afterwards and loop back
    to a fresh bag. After the first bag for the TSS, there are 3 ways to build the TST, and out of these, the first is
    the best, with a 69% chance to PC with 8 minimals. If the T comes first it becomes 94%. The second only has a 19.21%
    chance of PC, and PC is not possible for the third. If a PC is not achievable after the TST, a TSD into 7-2 or 6-3
    stacking is very easy.</p><br>
    
    <br><br><br><br><h3>COMBO OPENERS</h3>
    <h4>4-wide</h4>
    <a href="https://four.lol/stacking/4-wide"><img src="https://i.ibb.co/McbS4Xf/c4w.png" alt="c4w" border="0"></a><br>
    <p>Although there exists 2-wide and 3-wide, 4-wide can maintain the longest combo and is most commonly used. 
    Almost all line clears in a 4-wide is a single. The key to maintaining a combo chain with this setup is by clearing 
    lines in a manner so that you are left with a 1 hole gap for your next line clear, or 2 to 3 holes that are adjacent
    to each other or can be cleared with a single piece. This requires you to plan ahead an look at your piece previews 
    so that you can maintain the combo. <br>
    There are 2 types of 4W: C4W and S4W (center and side). These denote if your
    4-wide well is at the side or center. To make either 4-wide, stack up as high as you can on the side(s) of the well.
    If a piece is unable to fit, you can throw it in the well. Stacking a 4-wide, especially C4W, requires you to look
    at your piece previews as well. Although C4W is much harder to stack, you can receive 19 lines of garbage without
    topping out; a significant defensive advantage. <br><br>
    In modern tetris games such as tetr.io and jstris, after 9 lines
    cleared consecutively a lot of cheese (unclean lines) starts being sent over, and after 12 lines, 3 or 4 depending
    on client is sent over at a single line clear, the amount a tetris sends. If there is a multiplier function in the
    game e.g. tetr.io where the number of lines cleared before a tetris/ t-spin increases the number of lines it sends, 
    sending a tetris after you do a high combo could be lethal. <br>
    For example using tetr.io, at 10 combo, 14 lines are sent from the single line clears. 
    If a tetris is cleared after the 10 combo, the tetris does 10+4=14 damage, dealing a 28 spike
    in total.</p>
    
    <br><br><br><br>
    <p style='font-size:250%'>STUFF TO DO</p>
    <a href="/tetris">PLAY TETRIS</a>
    <br>
    <a href="/home">GO HOME</a>
    
    
    <p><br></p>
    <footer style="font-size:150%; color:yellow ">created by lim ao xuan</footer>
    </body>
    </html>
    ''')


def aoxuan(request):
    return HttpResponse('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Grammarly</title>
        <link href="data:image/x-icon;base64,AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADb1FgAx8H/ANvU/wD/9/8A//f/AP/
        3/wD/9/8A//f/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADb1FgAx8H/ANvU/wYPD/8GDw//Bg8P/wYPD/8GDw//AP/3/wD/9/8AAAAAAAA
        AAAAAAAAAAAAAAAAAAADb1FgAx8H/ANvU/wYPD/8GDw//Bg8P/wYPD/8rAP//KwD//wYPD/8A//f/AP/3/wAAAAAAAAAAAAAAAAAAAAAA29RYAMf
        B/wDb1P8GDw//Bg8P/wYPD/8GDw//Bg8P/ysA//8GDw//AP/3/wD/9/8AAAAAAAAAAAAAAAAA29RYAMfB/wDb1P8A//f/Bg8P/wYPD/8GDw//Bg8
        P/wYPD/8GDw//Bg8P/wD/9/8A//f/AP/3/wAAAAAAAAAAANvUWADHwf8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AP/
        3/wD/9/8AAAAAAAAAAADb1FgAx8H/ANvU/wD/9/8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AAAAAAAAAAAA29RYAMf
        B/wDb1P8A//f/AP/3/wYPD/8GDw//AP/3/wD/9/8A//f/Bg8P/wYPD/8A//f/AP/3/wAAAAAAAAAAANvUWADHwf8A//f/AP/3/wYPD//////////
        //wYPD/8A//f/Bg8P////////////Bg8P/wD/9/8AAAAAAAAAAAAAAAAA29RYAMfB/wD/9/8GDw///////wYPD/8GDw//AP/3/wYPD///////Bg8
        P/wYPD/8AAAAAAAAAAAAAAAAAAAAAANvUWADHwf8A29T/AP/3/wYPD/8GDw//AP/3/wD/9/8A//f/Bg8P/wYPD/8A//f/AAAAAAAAAAAAAAAAAAA
        AAAAAAAAA29RYAMfB/wDb1P8A//f/AP/3/wD/9/8A//f/AP/3/wD/9/8A//f/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADb1FgAx8H/ANv
        U/wD/9/8A//f/AP/3/wD/9/8A//f/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAA//8AAP//AADwHwAA4A8AAMAHAADABwAAgAMAAIADAACAAwAAgAMAAIADAADABwAAwAcAAOAPAADwHwAA//8
        AAA==" rel="icon" type="image/x-icon" />
    
    <style>
    body {background-color: black;}
    h1 {
       color: orange;
       font-family: comic sans ms;
       font-size: 300%;
    }

    h2 {
       color: orange;
       font-family: comic sans ms;
       font-size: 260%
    }

    h3 {
       color: orange;
       font-family: comic sans ms;
       font-size: 220%
    }

    h4 {
       font-family: comic sans ms;
       color: teal;
       font-size: 180%
    }

    p {
     font-family: comic sans ms;
     font-size: 140%;
     color: white;
    }

    a {
       color: green;
       font-family: comic sans ms;
       font-size: 200%;
    }

    </style>
    </head>
    <body>
    
    <header><h1>Ao Xuan</h1><header>
    <h2>the creator of this horrible website</h2>
    <h2 style="color:fuchsia">a supporter of comic sans ms</h2>
    
    <h3>this website is a useless website. fr.</h3><br><br>
    
    <h3>About Me</h3>
    <p>First, I shall introduce myself. My professional title is a human. I graduated from Planet Earth some 14 years
    ago. I have a lot of achievements and qualifications, including being a proud member of the species Homo Sapiens
    which currently is the most abundant and widespread primate. My goals are to, firstly, avoid WW3 from happening, 
    secondly, to remove tiktok from this world, and lastly, take over the world and become a dictator. I hope you will
    support me in this goal. Thank you. </p>
    <br>
    
    <h3>On the Topic Of Life and Grass</h3>
    <h4>The Basics</h4>
    <p>With my extreme qualifications as a human from Planet Earth, I believe I am suitable to humbly remind you to 
    touch grass and get a life. As unnerving and difficult it may seem, I assure you that it does not require much
    skill and anyone can easily achieve it; it is merely a matter of determination.</p><br>
    <br><p>1. Put down your device right now, be it phone or computer.</p>
    <br><p>2. Walk out of your room</p>
    <br><p>3. Open your door leading outside your house or to your residential building.</p>
    <br><p>4. Find a patch of healthy grass. Grass should look green. If it is purple, make sure that you have followed
    the above steps properly.</p>
    <br><p>5. Bow, or squat down, and extend your hand(s) to touch the grass.</p>
    <br><p>With the above simple 5 steps, you have successfully touched grass.</p>
    <br>
    
    <h4>The Advantages</h4>
    <p>Although one may not realise so, touching grass results in a lot of benefits both to your physical and mental
    health. The average being may spend 25 hours a day online, gaming or on social media. Although there is scientific
    research to state that this is unhealthy, using one's brain (organ of thought) may generate the same conclusion. The
    internet is unhealthy, and by touching grass, one will stop being addicted to it.</p><br>
    <br><p>1. It allows you to move your body, preventing numbness or aches.</p>
    <br><p>2. You will physically reconnect with the real world.</p>
    <br><p>3. Addiction to your device will reduce by an amount.</p>
    <br><p>4. You will realise that there is much more to life than the internet.</p>
    <br><p>5. Depending on the actions you take after this, you may or may not get a life.</p>
    <p></p>
    
    <a href="mailto:aoxuan66@gmail.com">contact me by email (aoxuan66@gmail.com)</a>
    <br><a href="https://www.youtube.com/channel/UCS7To04QXovZkctb5GLxoqw">my yt channel</a>
    <br>
    <br>
    <br><a href='/home/'>go home</a>
    <br><a href='/catalog/'>go to catalog</a>

    
    <p><br></p>
    <footer style="font-size:150%; color:yellow ">created by lim ao xuan</footer>
    </body>
    </html>
    ''')

