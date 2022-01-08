"""
##INIT##
#List of files to use as initial seed
file_list = [
    "F:\Documents\Bac 2 unamur\Q1\MOOC\problem_set_4\Test_1.pdf",
    "F:\Documents\Bac 2 unamur\Q1\MOOC\problem_set_4\Test_2.pdf"
]

#List of PDF readers
apps = [
    "C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe",
    "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
]

#output file
fuzz_output = "fuzz.pdf"

FuzzFactor = 250
num_tests = 10000

##PROGRAM##
import math
import random
import string
import subprocess
import time

for i in range(num_tests):
    #choose a random file and random program
    file_choice = random.choice(file_list)
    app = random.choice(apps)

    #store all file's bytes in a buffer
    buf = bytearray(open(file_choice, "rb").read())

    #total number of writes
    numwrites = random.randrange(math.ceil((float(len(buf)) / FuzzFactor)))+1

    #overwrite random actual bytes by random new ones
    for j in range(numwrites):
        rbyte = random.randrange(256)
        rn = random.randrange(len(buf))
        buf[rn] = "%c"%(rbyte)

    #writes these new bytes in a new file
    open(fuzz_output, "wb").write(buf)

    #open an application with the new file
    process = subprocess.Popen([app, fuzz_output])

    time.sleep(1)
    crashed = process.poll()
    if not crashed:
        process.terminate
"""


from genericpath import exists
import random, logging


def file_fuzzer(manual):
    """
    Fuzzer for the pdf reader to test

    Parameter
    ---------
    manual: true if the file is a user input
    """
    import math, subprocess, time

    #INITIALISATION

    print('Debut de l\'étape de fuzzing ...')
    logging.debug('Debut de l\'etape de fuzzing ...')

    if not manual: #seed contenant tous les fichiers dans le cas ou l'utilisateur ne rentre pas l'adresse
        test_files = [
            'Test_1.pdf', 'Test_2.pdf']
        selected_file = random.choice(test_files)
        selected_file_address = 'problem_set_4' + '\\' + 'fichiers_test'+'\\' + random.choice(test_files)
    else:
        selected_file_address = str(input('Donner l\'adresse du fichier à fuzz:')) #adresse du fichier donnée par l'utilisateur


    file_name = selected_file_address.split(".")
    if len(file_name) != 1: #extension pour fichier de sortie
        extension = file_name[(len(file_name) - 1)]
    else:
        extension = ""
    program_to_test = "/Applications/Zotero.app" #programme en version beta à tester


    #conversion en pdf dans le cas ou le fichier entré n'est pas un fichier pdf
    if extension != "pdf":
        extension = "pdf"

    print('Fuzzing du fichier %s avec le logiciel en cours ...'%(selected_file))
    logging.debug('Fuzzing du fichier %s avec le logiciel en cours ...'%(selected_file))


    #stocker les donées binaires du fichier choisi
    buffer = bytearray(open(selected_file_address, 'rb').read())

    #nombre de réécritures dans le buffer
    FuzzFactor = 250 # plus ce nombre est grand moins il y a de réécritures
    numwrites = random.randrange(math.ceil((float(len(buffer)) / FuzzFactor)))+1

    #phase de fuzzing (Code de Charlie Miller)

    for i in range(numwrites):
        rbytes = random.randrange(256) #byte aleatoire
        readnum = random.randrange(len(buffer)) #indice aléatoire dans le buffer
        buffer[readnum] = rbytes #remplacement du byte present

    print('Fin de l\'étape de fuzzing ...')
    logging.debug('Fin de l\'etape de fuzzing ...')

    #fichier de sortie
    output_file = "problem_set_4\\fuzz_output." + extension #fichier de sortie

    print('Ouverture du fichier de sortie en cours ...')
    logging.debug('Ouverture du fichier de sortie en cours ...')
    try:
        open(output_file, 'wb').write(buffer)
    except PermissionError:
        return

    #lire le fichier de sortie
    process = subprocess.Popen([program_to_test, output_file])

    #mettre fin au processus de lecture du fichier

    print('Fermeture du fichier de sortie en cours ...')
    logging.debug('Fermeture du fichier de sortie en cours ...')

    time.sleep(1)
    crashed = process.poll()
    if not crashed:
        process.terminate
    else:
        print('Un crash a eu lieu ...')
        logging.debug('Un crash a eu lieu ...')
    

def random_tester(max_num):
    """Random testing for the fuzzer
    
    Parameter:
    ----------
    max_num: max number of tests (should be > 0) (int)

    """
    assert max_num > 0

    num_test = random.randrange(max_num) #nombre total de tests durant le testing

    print('Il y aura un total de %d tests ...\n'%(num_test))
    logging.debug('Il y aura un total de %d tests ...\n'%(num_test))

    for i in range(num_test): #tests de fuzzing
        print('________Début du Fuzzing n°%d________'%(i + 1))
        logging.debug('________Debut du Fuzzing numero %d________'%(i + 1))
        fuzz_mode = str(input('Voulez vous fuzzer un fichier en particulier? (y/n)')) #avec fichier en particulier
        if fuzz_mode in['y', 'yes', 'o', 'oui']:
            logging.debug('Fuzz d\'un fichier choisi par l\'utilisateur')
            file_fuzzer(True)

        else: #avec fichier random
            logging.debug('Fuzz d\'un fichier aleatoire')
            file_fuzzer(False)
            
        print('_________Fin du Fuzzing n°%d_________\n\n'%(i + 1))
        logging.debug('_________Fin du Fuzzing numero %d_________\n\n'%(i + 1))

    print('Tous les tests ont été fait ...\n')
    logging.debug('Tous les tests ont ete fait ...\n')


    from os import remove

    #suppression des fichiers générés si possible

    print('Suppression du fichier généré en cours ...\n')
    logging.debug('Suppression du fichier genere en cours ...\n')

    if exists('problem_set_4\\fuzz_output.pdf'):
        try:
            remove('problem_set_4\\fuzz_output.pdf')
            print('Le fichier de sortie pdf a été supprimé ...')
            logging.debug('Le fichier de sortie pdf a ete supprime ...')

        except PermissionError:
            print('Erreur lors de la suppression du fichier de sortie pdf ...')
            logging.debug('Erreur lors de la suppression du fichier de sortie pdf ...')
    else:
        print('Impossible de supprimer fuzz_output.pdf ...\n')
        logging.debug('Impossible de supprimer fuzz_output.pdf ...\n')


    print('Fin de l\'étape de suppression du fichier ...\n\n')
    logging.debug('Fin de l\'etape de suppression du fichier ...\n\n')

#enregistrer les tests de fuzz dans un fichier de logs
logging.basicConfig(filename="problem_set_4\\random_tests.log", format='%(asctime)s %(message)s', level=logging.DEBUG)
logging.basicConfig(datefmt='%m/%d/%Y %I:%M:%S %p')

#random testing avec max 20 tests

print('___Random testing avec 20 tests___\n\n')
logging.debug('___Random testing avec 20 tests___\n\n')
random_tester(20)
