import urllib.request
import inquirer
import filenamecreator as fc
import os



questions = [
  inquirer.Text('imagenumber', message="Image Number"),
  inquirer.Text('height', message="Height(px)"),
  inquirer.Text('weight', message="Weight(px)"),

  inquirer.List('filename',
                message="Name my file as: ",
                choices=['uuid', 'ascending'],
            ),
            inquirer.Path('filepath',message="Output filepath: ", path_type=inquirer.Path.DIRECTORY,)
  ]

answers = inquirer.prompt(questions)

filenames = fc.fnc(answers['filename'],int(answers['imagenumber']))



for k in range(0,int(answers['imagenumber'])):
  fullfilename = os.path.join(answers['filepath'],str(filenames[k]))
  urllib.request.urlretrieve("http://picsum.photos/{}/{}".format(answers['height'],answers['weight']), "{}.png".format(fullfilename))

print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
