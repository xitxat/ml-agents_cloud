def speak(text, lang='en-US'):
    from IPython.display import Javascript as js, clear_output
    # Escape single quotes
    text = text.replace("'", r"\'")
    display(js(f'''
    if(window.speechSynthesis) {{
        var utterance = new window.SpeechSynthesisUtterance('{text}');
        utterance.lang = '{lang}';
        var synth = window.speechSynthesis;
        synth.speak(utterance);
    }}
    '''))
    # Clear the JS so that the notebook doesn't speak again when reopened/refreshed
    clear_output(False)

# usage :: speak("Cell completed!", lang='en-US')
