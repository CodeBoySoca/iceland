<!DOCTYPE html>
<html lang="en">
<head>
 <title>Iceland</title>
 <link rel="stylesheet" href="https://use.typekit.net/cli4tgl.css">
 <link rel="stylesheet" href="/static/css/main.css">
 <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js" integrity="sha512-894YE6QWD5I59HgZOGReFYm4dnWc1Qt5NtvYSaNcOP+u1T9qYdvdihz0PPSiiqn/+/3e7Jo4EaG7TubfWGUrMQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
 <script src="/static/js/main.js"></script>
</head>
<body>
<nav>
  <ul>
    <li><a href="{{ get_url('index') }}">home</a></li>
    <li><a href="{{ get_url('geography') }}">geography</a></li>
    <li><a href="{{ get_url('contact') }}">contact</a></li>
    <li><a href="{{ get_url('events') }}">events</a></li>
    <li><a href="{{ get_url('trade_and_invest') }}">trade and invest</a></li>
    <li><a href="{{ get_url('arts_and_culture') }}">arts and culture</a></li>
    <li><a href="{{ get_url('iceland_abroad') }}">iceland abroad</a></li>
  </ul>
</nav>
<div id="container">
   {{!base}}
</div>
</body>
</html>