<h1>DTextchange</h1>
<h3>General Information</h3>
<p>The DTextchange is a web-based textbook exchange designed to help Dartmouth students buy/sell used textbooks at a mutually beneficial price compared to other book re-sellers. The app is built on Flask using an MVC architecture and is divided as follows:</p>
<ol>
	<li>
		User Interface
		<ul>
			<li>Technologies: HTML5, CSS3, Bootstrap, JavaScript/jQuery, Flask/Jinja2 templating engine</li>
			<li></li>
		</ul>
	</li>
	<li>
		Controllers
		<ul>
			<li>Technologies: Python, Flask URL Mapping</li>
		</ul>
	</li>
	<li>
		Models
		<ul>
			<li>Technologies: currently MongoDB, look into SQLAlchemy porting for PostgreSQL, Python</li>
		</ul>
	</li>
</ol>

<h3>For Developers</h3>
<p>To run in development on local host:</p>
<ol>
  	<li>pull repository</li>
  	<li>cd to application root directory; execute run.py</li>
  	<li>go to localhost:5000/ via http in browser</li>
</ol>
<p>Best practices for committing changes:</p>
<ol>
	<li>Create a new branch on your local repository e.g. &lt;yourname&gt;/&lt;branchname&gt;</li>
	<li>Commit your changes locally and push your new branch to the GitHub repository.</li>
	<li>An admin after reviewing your changes will merge your branch into master, after which you can do a git pull and delete your old branch.</li>
</ol>

<h3>Misc</h3>
<ul>
	<h1>TODO:</h1>
	<li>Create user profile page</li>
	<li>Get access for Dartmouth student netID accounts</li>
	<li>Match ranking algorithm</li>
	<li>Search results page</li>
	<li>Port data models from MongoDB to PostgreSQL</li>
</ul>
