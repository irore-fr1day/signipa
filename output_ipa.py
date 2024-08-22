import os
import subprocess
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def select_file(filetype):
    filetypes = {
        'ipa': [('IPA files', '*.ipa')],
        'p12': [('P12 Certificate', '*.p12')],
        'mobileprovision': [('Mobile Provisioning Profile', '*.mobileprovision')]
    }
    return filedialog.askopenfilename(title=f'Select {filetype.upper()}', filetypes=filetypes[filetype])

def sign_ipa(ipa_path, p12_path, mobileprovision_path, password):
    try:
        output_ipa = os.path.splitext(ipa_path)[0] + '_signed.ipa'
        command = [
            '/Users/max/Desktop/zsign/zsign/build/zsign',
            '-k', p12_path,
            '-p', password,
            '-m', mobileprovision_path,
            '-o', output_ipa,
            ipa_path
        ]
        subprocess.check_call(command)
        messagebox.showinfo("Success", f"IPA signed successfully!\nOutput file: {output_ipa}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Signing failed: {str(e)}")

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    ipa_path = select_file('ipa')
    if not ipa_path:
        return
    
    p12_path = select_file('p12')
    if not p12_path:
        return
    
    mobileprovision_path = select_file('mobileprovision')
    if not mobileprovision_path:
        return

    password = simpledialog.askstring("Password", "Enter the password for the .p12 file:", show='*')
    if not password:
        return

    sign_ipa(ipa_path, p12_path, mobileprovision_path, password)

if __name__ == '__main__':
    main()
