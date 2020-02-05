import urllib.request
import inquirer
import filenamecreator as fc



questions = [
  inquirer.Text('imagenumber', message="Image Number"),
  inquirer.Text('height', message="Height(px)"),
  inquirer.Text('weight', message="Weight(px)"),

  inquirer.List('filename',
                message="Name my file as: ",
                choices=['uuid', 'ascending'],
            ),
  ]

answers = inquirer.prompt(questions)

filenames = fc.fnc(answers['filename'],int(answers['imagenumber']))



for k in range(0,int(answers['imagenumber'])):
    urllib.request.urlretrieve("http://picsum.photos/{}/{}".format(answers['height'],answers['weight']), "{}.png".format(filenames[k]))

print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
