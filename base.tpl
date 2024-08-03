<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Prerequisites for ScrapeU</title>
<!DOCTYPE html>

<body>
    <h1>Enter Scraper Settings</h1>
    <form action="/submit" method="post">
        Base URL: <input type="text" name="base_url" value="https://www.linkedin.com/" /><br/>
        Search URL: <input type="text" name="search_url" /><br/>
        Chromedriver Path: <input type="text" name="chromedriver_path" /><br/>
        Email: <input type="email" name="email" /><br/>
        Password: <input type="password" name="password" /><br/>
        Location: <input type="text" name="search_location" /><br/>
        <input type="submit" value="Run Scraper" />
    </form>
</body>
</html>