<h1>Pracuj.pl Automated Tests Repository</h1>
<p>
    This repository contains automated tests for Pracuj.pl, a job search website. The tests are implemented using Selenium, a popular testing framework for web applications.
</p>

<h2>Getting Started</h2>
<p>
    To get started, make sure you have Python 3 installed on your machine. Additionally, you'll need to install the Selenium package and the appropriate WebDriver for your preferred browser (e.g., ChromeDriver).
</p>
<p>
    Clone this repository to your local machine:
</p>
<pre><code>git clone https://github.com/Martabtk/pracuj-pl-tests.git</code></pre>
<p>
    Install the required dependencies using the provided <code>requirements.txt</code> file:
</p>
<pre><code>pip install -r requirements.txt</code></pre>
<p>
    Once the dependencies are installed, you can execute the test suite by running the <code>test_suite.py</code> file:
</p>
<pre><code>python test_suite.py</code></pre>

<h2>Test Structure</h2>
<ul>
  <li><strong>test_demo_first_page:</strong> Verifies the title of the Pracuj.pl home page.</li>
  <li><strong>test_button_click:</strong> Tests the functionality of a specific button on the website.</li>
  <li><strong>test_job_search:</strong> Performs a job search and counts the number of job offers.</li>
  <li><strong>test_register_account:</strong> Tests the registration process for a new account.</li>
</ul>

