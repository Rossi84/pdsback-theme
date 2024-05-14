# Portale delle segnalazioni BACK docs theme

This is the official theme for any piece of documentation of Portale delle segnalazioni.

## How to use Sphinx CW theme on your documentation

* Add the following line to your documentation `requirements.txt` file:

    ```
    $ pip install git+https://github.com/Rossi84/pdsback-theme.git
    ```

* In your `conf.py` file, you'll need to specify the theme as follows:

    ```
    # Add this line at the top of the file within the "import" section
    import pdsback_theme

    # Add the Sphinx extension 'pdsback_theme' in the extensions list
    extensions = [
      ...,
      'pdsback_theme'
    ]

    # Edit these lines
    html_theme = "pdsback_theme"
    html_theme_path = [pdsback_theme.get_html_theme_path()]
    ```