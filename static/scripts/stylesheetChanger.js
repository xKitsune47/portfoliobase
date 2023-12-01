function changingStyles() {
    let cb = document.querySelector('#stylesheetChanger');
    let theme = document.getElementsByTagName('link')[2];
    if (cb.checked) {
        theme.setAttribute('href', "../static/css/styleLight.css");
        console.log('changing to dark mode');
    } else {
        theme.setAttribute('href', "../static/css/styleDark.css");
        console.log('changing to light mode');
    }
}
