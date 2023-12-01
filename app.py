from flask import Flask, render_template
import os


def siteContent():
    blockDict = {
        'block1': [placeholderImg, placeholderDescription],
        'block2': [placeholderImg, placeholderDescription],
        'block3': [placeholderImg, placeholderDescription]
    }
    return blockDict


app = Flask(__name__)
placeholderDescription = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ut molestie erat, vitae consequat arcu. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur dapibus augue eu dictum malesuada. '
placeholderImg = '../static/imgs/placeholder.jpg'


@app.route('/')
def siteDefaultTheme():
    return render_template('index.html', content=placeholderDescription, image=placeholderImg,
                           blockDict=siteContent(), stylesheet='light')


@app.route('/darkMode')
def siteDarkTheme():
    return render_template('index.html', content=placeholderDescription, image=placeholderImg,
                           blockDict=siteContent(), stylesheet='dark')


if __name__ == '__main__':
    app.run()
