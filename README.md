<h2>Mailer-Automation-ADB</h2>
<p>This is a Discord bot that sends SMS messages using a Google Spreadsheet.</p>

<h3>Requirements</h3>
<ul>
  <li>Python 3.x</li>
  <li>The following Python libraries:
    <ul>
      <li>discord</li>
      <li>requests</li>
      <li>gspread</li>
      <li>oauth2client</li>
    </ul>
  </li>
</ul>

<h3>Setup</h3>
<ol>
  <li>Make sure you have the required libraries installed. You can install them using the following command:</li>
</ol>

<pre><code>pip install discord requests gspread oauth2client</code></pre>

<ol start="2">
  <li>Download the JSON credentials file from the Google account service and save it as <code>credentials.json</code>. You can obtain these credentials by following the steps in the Google Drive API documentation.</li>
  <li>Open the <code>bot.py</code> file and replace the following values:
    <ul>
      <li><strong>SHEET-URL-HERE:</strong> Replace this with the URL of the Google Spreadsheet that contains the phone numbers.</li>
      <li><strong>DISCORD-BOT-API:</strong> Replace this with the Discord bot API token.</li>
    </ul>
  </li>
</ol>

<h3>ADB and shellms Dependencies</h3>
<p>The bot utilizes ADB (Android Debug Bridge) and the <a href="https://github.com/try2codesecure/ShellMS">shellms</a> package for sending SMS messages. Make sure you have ADB installed on your system and the <code>shellms</code> package available. You can install ADB by following the instructions specific to your operating system.</p>

<h3>Usage</h3>
<ol start="4">
  <li>Run the <code>bot.py</code> file:</li>
</ol>

<pre><code>python bot.py</code></pre>

<ol start="5">
  <li>In Discord, use the <code>/sendout</code> command to send a message. The bot will prompt you to enter the message to send.</li>
  <li>The bot will send the message to the phone numbers specified in the Google Spreadsheet.</li>
</ol>

<p>That's it! Now you can use the bot to send SMS messages through Discord.</p>

<p>Please note that this project is an example and may require modifications to fit your specific needs.</p>

<p>I hope this is what you're looking for. If you have any other questions, feel free to ask.</p>
