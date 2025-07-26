from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to Deepali's Portfolio</h1>
    <p>Explore the sections below:</p>
    <ul>
        <li><a href="/info">My Info</a></li>
        <li><a href="/projects">My Projects</a></li>
        <li><a href="/social">Social Media</a></li>
    </ul>
    """

@app.route("/info")
def lwcontact():
    return """
    <h2>About Me</h2>
    <p><strong>Name:</strong> Deepali Pateriya</p>
    <p><strong>Contact:</strong> +91-9829111111</p>
    <p><strong>Email:</strong> pateriyadeepali1008@gmail.com</p>
    <p>I am an aspiring DevOps Engineer with strong interest in cloud, automation, and CI/CD pipelines.<br>
    I love solving problems and building scalable systems.</p>
    <a href="/">← Go back</a>
    """

@app.route("/projects")
def projects():
    return """
    <h2>My Projects</h2>
    <ul>
        <li><a href="https://github.com/pateriyadeepali/polyglot_microservice_application" target="_blank">Polyglot Microservice Application</a></li>
        <li><a href="https://github.com/pateriyadeepali/Image_captioning" target="_blank">Image Captioning using Deep Learning</a></li>
        <li><a href="https://github.com/pateriyadeepali/techdome-assignment" target="_blank">Techdome DevOps Assignment</a></li>
    </ul>
    <a href="/">← Go back</a>
    """

@app.route("/social")
def social():
    return """
    <h2>My Social Media</h2>
    <ul>
        <li><a href="https://www.linkedin.com/in/deepali-pateriya2003/" target="_blank">LinkedIn</a></li>
        <li><a href="https://medium.com/@pateriyadeepali1008" target="_blank">Medium</a></li>
        <li><a href="https://github.com/pateriyadeepali" target="_blank">GitHub</a></li>
    </ul>
    <a href="/">← Go back</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
