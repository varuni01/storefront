import polib
from googletrans import Translator
import traceback

def translate_text(text, dest_language):
    translator = Translator()
    result = translator.translate(text, dest=dest_language)
    return result.text

def translate_po_file(po_file_path, dest_language='fr'):
    try:
        po = polib.pofile(po_file_path)

        if not po:
            raise Exception("PO file is empty or corrupted.")

        for entry in po:
            if any(file.startswith('lang/templates/home.html') for file, _ in entry.occurrences):
                print(f"Processing entry: {entry.msgid}")  # Debug print
                if entry.msgstr is None or entry.msgstr.strip() == "":
                    try:
                        translated_text = translate_text(entry.msgid, dest_language)
                        entry.msgstr = translated_text
                        print(f'Translated: {entry.msgid} -> {entry.msgstr}')
                    except Exception as e:
                        print(f"Error during translation: {e}")

                '''if entry.msgid_plural:
                    for idx, msgid in enumerate(entry.msgid_plural):
                        if entry.msgstr_plural[idx] is None or entry.msgstr_plural[idx].strip() == "":
                            try:
                                plural_translation = translate_text(msgid, dest_language)
                                entry.msgstr_plural[idx] = plural_translation
                                print(f'Translated plural: {msgid} -> {entry.msgstr_plural[idx]}')
                            except Exception as e:
                                print(f"Error during translation: {e}")'''

        po.save(po_file_path)
    except Exception as e:
        print(f"Error processing .po file: {e}")
        print(traceback.format_exc())

po_file_path = '/home/desktop/storefront/lang/locale/fr/LC_MESSAGES/django.po'
translate_po_file(po_file_path, 'fr')
