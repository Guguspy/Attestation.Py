 ###############################   IMPORT   ###############################

    #to get time

import datetime
from time import strftime
from time import gmtime, strftime


    #for pause

import time


    #for qrcode

import qrcode

    # cmd os
import os

    #for get line -> text

import linecache


    #for send email

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import mimetypes
import email.mime.application


    #for tkinter

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


    #for PDF

from reportlab.pdfgen import canvas 

from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

from reportlab.lib import colors

from PyPDF2 import PdfFileWriter, PdfFileReader

import io

from reportlab.lib.pagesizes import letter


    #pour eviter les erreurs en .exe
##import pkg_resources.py2_warn


###############################

###############################   CODE   ###############################

###########   DEF   ###########

def clean():
    os.remove('Attestation.pdf')
    os.remove('Qrcode.png')

def about():
    messagebox.showinfo("About","------------------------------\n|  REVERDY Guillaume  |\n------------------------------\n\n\n > BTS : SIO option SLAM\n\nSite internet : --en_cours--\n\nThanks to use my apps !\n\n\nHave a nice day !")

def generate_dat():
    fichier_new_profiledat = open('[+]/[PROFILES].dat','a')
    fichier_new_profiledat.close
    fichier_new_profiledat = open('[+]/[PROFILES].dat','w')
    fichier_new_profiledat.write('#  | Listes des profiles |\n')
    fichier_new_profiledat.write('#    Voilà comment doit être le document\n')
    fichier_new_profiledat.write('#    pour que votre profil soit bien importé :\n')
    fichier_new_profiledat.write('#    [NOM_PROFILE] (Peu importe le nom, il sera affiché dans la liste des résultats)\n')
    fichier_new_profiledat.write('#    NOM (Votre nom)\n')
    fichier_new_profiledat.write('#    PRENOM (Votre prénom)\n')
    fichier_new_profiledat.write('#    DATE/DE/NAISSANCE (Votre date de naissance en format : jj/mm/aaaa)\n')
    fichier_new_profiledat.write('#    VILLE_NAISSANCE (Votre ville de NAISSANCE)\n')
    fichier_new_profiledat.write('#    ADRESSE (Votre adresse sans le code postal, ni la ville)\n')
    fichier_new_profiledat.write('#    CODE_POSTAL (Votre code postal)\n')
    fichier_new_profiledat.write('#    VILLE (Votre ville)\n')
    fichier_new_profiledat.write('#    MAIL (Votre adresse mail à laquelle vous seront envoyé les documents (qrcode et attestation))\n')
    fichier_new_profiledat.write('#\n')
    fichier_new_profiledat.write('#    ^ et un espace pour faire joli :)\n')
    fichier_new_profiledat.write('#\n')
    fichier_new_profiledat.write('#    Si besoin d\'aide supplémentaires :\n')
    fichier_new_profiledat.write('#    Mail : reverdyguillaume73@gmail.com\n')
    fichier_new_profiledat.write('#    Discord : Gugus le Pingouin#0547\n')
    fichier_new_profiledat.write('\n')
    fichier_new_profiledat.write('')
    fichier_new_profiledat.close()

def centre_daides():
    centre_daides_fenetre = Toplevel(app)
    try:
        centre_daides_fenetre.iconbitmap('[+]/ico.ico')
    except:
        pass

        #Centrer fenetre tkinter
    screen_x = centre_daides_fenetre.winfo_screenwidth()
    screen_y = centre_daides_fenetre.winfo_screenheight()
    windows_x = 550
    windows_y= 200

    posX = (screen_x // 2)- (windows_x //2)
    posY = (screen_y // 2)- (windows_y //2)
    geo= "{}x{}+{}+{}".format(windows_x, windows_y, posX, posY)

    centre_daides_fenetre.geometry(geo)

        #redimensionable = False
    centre_daides_fenetre.resizable(width=False, height=False)
    
    resultframe = LabelFrame(centre_daides_fenetre, text='[Aides]',font=("Comic Sans MS","10","italic" ))
    resultframe.grid(row=0, column=0, pady=15, padx=30)
    
        #Bouton
    buttonframe = LabelFrame(resultframe, text='[Error profiles]',font=("Comic Sans MS","8","italic" ))
    buttonframe.grid(row=0, column=0, pady=15, padx=30)
    valid_btn = Button(buttonframe, text=" Générer .DAT ", command=generate_dat,font=("Comic Sans MS","12" ), borderwidth='5px',cursor='iron_cross')
    valid_btn.grid(row=0, column=0, pady=15, padx=30)

        #Bouton
    buttonframe = LabelFrame(resultframe, text='[Other info]',font=("Comic Sans MS","8","italic" ))
    buttonframe.grid(row=0, column=1, pady=15, padx=30)
    valid_btn = Button(buttonframe, text=" About me ", command=about,font=("Comic Sans MS","12" ), borderwidth='5px',cursor='iron_cross')
    valid_btn.grid(row=0, column=0, pady=15, padx=30)

def sendmail():
    global mail

    try:
        smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
        smtp_ssl_port = 465
        s = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        s.login('MAIL','PASS')
        #rentrez ici votre mail et votre password, mais veuillez d'abord désactiver la sécurité sur google (sinon ça ne marchera pas) compte -> securité -> Accès moins sécurisé des applications -> activer

        msg = MIMEMultipart()
        msg['Subject'] = 'Votre attestation'
        msg['From'] = 'attestation.py@gmail.com'
        msg['To'] = mail #destinataire

        txt = MIMEText('Veuillez trouver ci-joint votre attestion et votre qrcode : '+nom+' '+prenom+'.')#changez le texte comme bon vous semble
        msg.attach(txt)

        filename = 'Attestation.pdf' #path to file
        fo=open(filename,'rb')
        attach = email.mime.application.MIMEApplication(fo.read(),_subtype="pdf")
        fo.close()
        attach.add_header('Content-Disposition','attachment',filename=filename)
        msg.attach(attach)

        filename = 'Qrcode.png' #path to file
        fo=open(filename,'rb')
        attach = email.mime.application.MIMEApplication(fo.read(),_subtype="png")
        fo.close()
        attach.add_header('Content-Disposition','attachment',filename=filename)
        msg.attach(attach)
        s.send_message(msg)
        s.quit()
        messagebox.showinfo("No error","Attestation envoyé par mail à "+mail)
        os.remove('Attestation.pdf')
        os.remove('Qrcode.png')
    except:
        messagebox.showerror("Error","Vérifier votre connexion, si le problème persiste, contactez moi sur discord")


def create_pdf():
    global datemnn
    global date
    global dateyear
    global datehourr
    global datehour
    global datemn
    global dayy
    global dateday
    global datemonth
    global monthh
    global cbox
    global motif
    global pbox
    global dbox
    global tbox
    global qbox
    global cbox
    global sbox
    global ssbox
    global hbox
    global nbox
    
    
    box='[+]/box.png'
    vbox='[+]/vbox.png'
    sibox='signature.png'
    qrpng='Qrcode.png'
    pbox = box
    dbox = box
    tbox = box
    qbox = box
    cbox = box
    sbox = box
    ssbox = box
    hbox = box
    nbox = box
    motif=''

    date = datetime.datetime.now()

    date = datetime.datetime.now()
    str(date)
    dateyear = str(date.year)
    datehourr=date.hour
    datehour=str(date.hour)
    datemnn = date.minute + 1
    datemn=date.minute

    
    if datemnn == 60 :
        datemnn=0
    else:
        datemnn=datemn

    if datemnn==0:
        datehourr=datehourr+1
    else:
        datehourr=datehourr


    datemnn = date.minute + 1
    if datemnn == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
        datemnn=str(datemnn).zfill(2)
    else:
        datemnn=str(datemnn)

    if datehourr == 24:
        datehourr=0
    else:
        datehourr=datehourr

    
    datemnn=str(datemnn)
    minute = date.minute
    datehourr=str(datehourr)

    dayy= date.day

    monthh = date.month 
    
    if minute == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
        datemn=str(minute).zfill(2)
    else:
        datemn=str(minute)

    if dayy == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
        dateday= str(dayy).zfill(2)
    else:
        dateday= str(dayy)

    if monthh == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
        datemonth= str(monthh).zfill(2)
    else:
        datemonth= str(monthh)

    if var.get()==0 :
        pbox = vbox
        motif='travail'
    elif var.get()==1:
        dbox = vbox
        motif='achats'
    elif var.get()==2:
        tbox = vbox
        motif='sante'
    elif var.get()==3:
        qbox = vbox
        motif='famille'
    elif var.get()==4:
        cbox = vbox
        motif='handicap'
    elif var.get()==5:
        sbox = vbox
        motif='sport_animaux'
    elif var.get()==6:
        ssbox = vbox
        motif='convation'
    elif var.get()==7:
        hbox = vbox
        motif='missions'
    elif var.get()==8:
        nbox = vbox
        motif='enfants'


        # Qrcode
    qrrr='Cree le: '+dateday+'/'+datemonth+'/'+dateyear+' a '+datehourr+'h'+datemnn+';\n Nom: '+nom+';\n Prenom: '+prenom+';\n Naissance: '+datenaissance+' a '+lieunaissance+';\n Adresse: '+residence+' '+codepostal+' '+ville+';\n Sortie: '+dateday+'/'+datemonth+'/'+dateyear+' a '+datehour+'h'+datemn+';\n Motifs: '+motif
    #print(str(qrrr))
    img = qrcode.make(qrrr)
    img.save('Qrcode.png')

##
##    packet = io.BytesIO()
##    # create a new PDF with Reportlab
##    can = canvas.Canvas(packet, pagesize=letter)
##    
##    can.drawString(107, 657, prenom+' '+nom)
##    can.drawString(535, 656,',')
##    can.drawString(107, 627,datenaissance)
##    can.drawString(240, 627,lieunaissance)
##    can.drawString(535, 626,',')
##    can.drawString(125, 596,residence+' '+codepostal+' '+ville)
##    can.drawString(535, 595,',')
##    
##    can.drawString(93, 122,ville)
##    can.drawString(535, 121,',')
##    can.drawString(77, 92,dateday +'/' +datemonth +'/' +dateyear)
##    can.drawString(245, 92,datehour +':'+datemn)
##    can.drawString(362, 91,'.')
##    
##            # Draw image
##
##    try:
##        can.drawInlineImage(pbox, 57, 485, width=11, height=11)
##        can.drawInlineImage(dbox, 57, 415, width=11, height=11)
##        can.drawInlineImage(tbox, 57, 344, width=11, height=11)
##        
##        can.drawInlineImage(qbox, 57, 322, width=11, height=11)
##        can.drawInlineImage(cbox, 57, 289, width=11, height=11)
##        can.drawInlineImage(sbox, 57, 267, width=11, height=11)
##        
##        can.drawInlineImage(ssbox, 57, 197, width=11, height=11)
##        can.drawInlineImage(hbox, 57, 176, width=11, height=11)
##        can.drawInlineImage(nbox, 57, 154, width=11, height=11)
##    except:
##        messagebox.showerror("Error","Des images sont manquantes dans le dossier [+]")
##        clean()
##    
##    can.drawInlineImage(qrpng, 435, 20, width=100, height=100)
##    
##    can.save()
##
##    packet.seek(0)
##    new_pdf = PdfFileReader(packet)
##    # read your existing PDF
##    existing_pdf = PdfFileReader(open("[+]\original.pdf", "rb"))
##    output = PdfFileWriter()
##    # add the "watermark" (which is the new pdf) on the existing page
##    page = existing_pdf.getPage(0)
##    page.mergePage(new_pdf.getPage(0))
##    output.addPage(page)
##    # finally, write "output" to a real file
##    outputStream = open("Attestation.pdf", "wb")
##    output.write(outputStream)
##    outputStream.close()


        # Content
    fileName = 'Attestation.pdf'
    documentTitle = 'dérogation'
    title = 'ATTESTATION DE DÉPLACEMENT DÉROGATOIRE'
    subTitle = 'En application du décret no 2020-1310 du 29 octobre 2020 prescrivant les mesures générales nécessaires' 
    subtitle = 'pour faire face à l’épidémie de COVID-19 dans le cadre de l’état d’urgence sanitaire'

    textLines1_1 = [
    'Mme/M. : '+prenom+' '+nom,
    ]

    textLines1_2 = [
    'Né(e) le : '+datenaissance+ '                à : '+lieunaissance,
    ]

    textLines1_3 = [
    'Demeurant : '+residence+' '+codepostal+' '+ville,
    ]

    textLines1_4 = [
    'Fait à : '+ville,
    ]
    
    textLines1_5 = [
    'Le : ' +dateday +'/' +datemonth +'/' +dateyear +'                                  à : '+datehour +':'+datemn,
    ]

    textLines1_6 = [
    '(Date et heure de début de sortie à mentionner obligatoirement)',
    ]


    textLines2 = [
    '1. Déplacements entre le domicile et le lieu d’exercice de l’activité professionnelle ou un établissement',
    'd’enseignement ou de formation ; déplacements professionnels ne pouvant être différés ; déplacements',
    'pour un concours ou un examen ;',
    '',
    '',
    '',
    '2. Déplacements pour se rendre dans un établissement culturel autorisé ou un lieu de culte ;',
    'déplacements pour effectuer des achats de biens, pour des services dont la fourniture est autorisée, pour',
    'les retraits de commandes et les livraisons à domicile ;',
    '',
    '3. Consultations, examens et soins ne pouvant être assurés à distance et achats de médicaments ;',
    '',
    '4. Déplacements pour motif familial impérieux, pour l’assistance aux personnes vulnérables et précaires',
    'ou la garde d’enfants ;',
    '',
    '5. Déplacements des personnes en situation de handicap et leur accompagnant ;',
    '',
    '6. Déplacements en plein air ou vers un lieu de plein air, sans changement du lieu de résidence, dans la',
    'limite de trois heures quotidiennes et dans un rayon maximal de vingt kilomètres autour du domicile, liés',
    'soit à l’activité physique ou aux loisirs individuels, à l’exclusion de toute pratique sportive collective et',
    'de toute proximité avec d’autres personnes, soit à la promenade avec les seules personnes regroupées',
    'dans un même domicile, soit aux besoins des animaux de compagnie ;',
    '',
    ' 7. Convocations judiciaires ou administratives et déplacements pour se rendre dans un service public ;',
    '',
    '8. Participation à des missions d’intérêt général sur demande de l’autorité administrative ;',
    '',
    '9. Déplacements pour chercher les enfants à l’école et à l’occasion de leurs activités périscolaires ;',
    ]

    textLines3 = [
    'Note : Les personnes souhaitant bénéficier de l’une de ces exceptions doivent se munir s’il y a lieu, lors de leurs déplacements hors',
    'de leur domicile, d’un document leur permettant de justifier que le déplacement considéré entre dans le champ de l’une de ces',
    'exception',
    ]
    
    textLines4 = [
    'certifie que mon déplacement est lié au motif suivant (cocher la case) autorisé par le décret no',
    '2020-1310 du 29 octobre 2020 prescrivant les mesures générales nécessaires pour faire face à',
    'l’épidémie de COVID-19 dans le cadre de l’état d’urgence sanitaire :',
    ]

    textLines5 = [
    'Note : A utiliser par les travailleurs non-salariés, lorsqu’ils ne peuvent disposer d’un justificatif de déplacement établi par leur',
    'employeur.',
    ]

    textLines6 = [
    ]



    Textlines = [
        
    ]


    box = '[+]/box.png'

    vbox = '[+]/vbox.png'

    qrpng = 'Qrcode.png'

    
        # Create document 
    pdf = canvas.Canvas(fileName)
    pdf.setTitle(documentTitle)

    pdfmetrics.registerFont(
        TTFont('Trebuchet_MS_Bold', '[+]\[FONT]\[TITLE]\\font.ttf')
    )

        # Set fonts Title
    pdf.setFillColorRGB(0, 0, 0)
    pdf.setFont("Trebuchet_MS_Bold", 15)#Times-Bold
    pdf.drawCentredString(300, 780, title)

    # Sub Title

    pdfmetrics.registerFont(
        TTFont('Trebuchet_MS_Italic', '[+]\[FONT]\[SUBTITLE]\\font.ttf')
    )

    pdf.setFillColorRGB(0, 0, 0)
    pdf.setFont("Trebuchet_MS_Italic", 10.5)
    pdf.drawCentredString(300,755, subTitle)


        
    pdf.setFillColorRGB(0, 0, 0)
    pdf.setFont("Trebuchet_MS_Italic", 10.5)
    pdf.drawCentredString(300,742, subtitle)



    pdfmetrics.registerFont(
        TTFont('Trebuchet_MS', '[+]\[FONT]\[TEXT]\\font.ttf')
    )


        # Text object
    from reportlab.lib import colors

    text = pdf.beginText(43, 700)
    text.setFont("Trebuchet_MS", 11)
    text.setFillColor(colors.black)
    for line in textLines1_1:
        text.textLine(line)
    
    pdf.drawText(text)


    text = pdf.beginText(43, 680)
    text.setFont("Trebuchet_MS", 11)
    text.setFillColor(colors.black)
    for line in textLines1_2:
        text.textLine(line)

    pdf.drawText(text)


    text = pdf.beginText(43, 660)
    text.setFont("Trebuchet_MS", 11)
    text.setFillColor(colors.black)
    for line in textLines1_3:
        text.textLine(line)

    pdf.drawText(text)

    text = pdf.beginText(43, 80)
    text.setFont("Trebuchet_MS", 10)
    text.setFillColor(colors.black)
    for line in textLines1_4:
        text.textLine(line)

    pdf.drawText(text)

    text = pdf.beginText(43, 60)
    text.setFont("Trebuchet_MS", 10)
    text.setFillColor(colors.black)
    for line in textLines1_5:
        text.textLine(line)

    pdf.drawText(text)

    text = pdf.beginText(43, 40)
    text.setFont("Trebuchet_MS", 10)
    text.setFillColor(colors.black)
    for line in textLines1_6:
        text.textLine(line)

    pdf.drawText(text)



    Text2 = pdf.beginText(60, 555)
    Text2.setFont("Trebuchet_MS", 10)
    Text2.setFillColor(colors.black)
    for line in textLines2:
        Text2.textLines(line)

    pdf.drawText(Text2)


    Text3 = pdf.beginText(43, 599)
    Text3.setFont("Trebuchet_MS", 8)
    Text3.setFillColor(colors.black)
    for line in textLines3:
        Text3.textLines(line)

    pdf.drawText(Text3)


    Text4 = pdf.beginText(43, 637)
    Text4.setFont("Trebuchet_MS", 10)
    Text4.setFillColor(colors.black)
    for line in textLines4:
        Text4.textLines(line)

    pdf.drawText(Text4)

    Text5 = pdf.beginText(60, 520)
    Text5.setFont("Trebuchet_MS", 7)
    Text5.setFillColor(colors.black)
    for line in textLines5:
        Text5.textLines(line)

    pdf.drawText(Text5)

    Text6 = pdf.beginText(332, 517)
    Text6.setFont("Trebuchet_MS", 7)
    Text6.setFillColor(colors.black)
    for line in textLines6:
        Text6.textLines(line)

    pdf.drawText(Text6)


        # Draw image

    try:
        pdf.drawInlineImage(pbox, 45, 553, width=10, height=10)
        pdf.drawInlineImage(dbox, 45, 481, width=10, height=10)
        pdf.drawInlineImage(tbox, 45, 433, width=10, height=10)
        
        pdf.drawInlineImage(qbox, 45, 409, width=10, height=10)
        pdf.drawInlineImage(cbox, 45, 373, width=10, height=10)
        pdf.drawInlineImage(sbox, 45, 350, width=10, height=10)
        
        pdf.drawInlineImage(ssbox, 45, 278, width=10, height=10)
        pdf.drawInlineImage(hbox, 45, 254, width=10, height=10)
        pdf.drawInlineImage(nbox, 45, 229, width=10, height=10)
    except:
        messagebox.showerror("Error","Des images sont manquantes dans le dossier [+]")
        clean()
    
    pdf.drawInlineImage(qrpng, 435, 25, width=100, height=100)
    pdf.save()

    #print('Attestation crée !')
    time.sleep(1.500)

    sendmail()
    #sendmail1()

def sendmail1():
    pass


def search_string_in_file(file_name, string_to_search):
    """Search for the given string in file and return lines containing that string,
    along with line numbers"""
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            if string_to_search in line:
                # If yes, then add the line number & line as a tuple in the list
                list_of_results.append((line_number, line.rstrip()))
    # Return list of tuples containing line numbers and lines where string is found
    return list_of_results

def configpdfprofile():
    global lineprofileselect
    global choixprofilend

    global nom
    global prenom
    global datenaissance
    global lieunaissance
    global residence
    global codepostal
    global ville
    global mail
    

    choixprofilend=listshowprofiles.get(ANCHOR)
    
    matched_lines = search_string_in_file('[+]/[PROFILES].dat',choixprofilend)
    for elem in matched_lines:
        lineprofileselect= elem[0]

    #print('')
    
    lineprofileselect=lineprofileselect+1     
    nom=linecache.getline('[+]/[PROFILES].dat',lineprofileselect)
    nom=nom[:-1]
    #print(nom)
    
    lineprofileselect=lineprofileselect+1     
    prenom=linecache.getline('[+]/[PROFILES].dat',lineprofileselect)
    prenom=prenom[:-1]
    #print(prenom)
    
    lineprofileselect=lineprofileselect+1     
    datenaissance=linecache.getline('[+]/[PROFILES].dat',lineprofileselect)
    datenaissance=datenaissance[:-1]
    #print(datenaissance)
    
    lineprofileselect=lineprofileselect+1     
    lieunaissance=linecache.getline('[+]/[PROFILES].dat',lineprofileselect)
    lieunaissance=lieunaissance[:-1]
    #print(lieunaissance)
    
    lineprofileselect=lineprofileselect+1     
    residence=linecache.getline('[+]/[PROFILES].dat',lineprofileselect)
    residence=residence[:-1]
    #print(residence)

    lineprofileselect=lineprofileselect+1     
    codepostal=linecache.getline('[+]/[PROFILES].dat',lineprofileselect)
    codepostal=codepostal[:-1]
    #print(codepostal)

    lineprofileselect=lineprofileselect+1     
    ville=linecache.getline('[+]/[PROFILES].dat',lineprofileselect)
    ville=ville[:-1]
    #print(ville)
    
    lineprofileselect=lineprofileselect+1     
    mail=linecache.getline('[+]/[PROFILES].dat',lineprofileselect)
    mail=mail[:-1]
    #print(mail)

    if mail=='':
        messagebox.showerror("Error","Veuillez selectionner un profil !")
    else:
        create_pdf()


def showinfotxt():
    global nodatdata
    global listevide
    global listeprofile
    global choixprofilend
    
        # nothing = blank
    nodatdata=False
    nothing=""
    listevide=[]
    listeprofile=[]
    profiletxtcount=0
    #print('')
    detecttextprofiles1='['
    detecttextprofiles2=']'
    detecttextprofiles3='#'
    try:
        fichier1profiles = open("[+]/[PROFILES].dat","r")
        for ligneprofiles in fichier1profiles:
            if detecttextprofiles1 in ligneprofiles and detecttextprofiles2 in ligneprofiles and not detecttextprofiles3 in ligneprofiles:
                try:
                    profiletxtcount=profiletxtcount+1
                    strprofiletxtcount=str(profiletxtcount)

                    ligneprofiles=ligneprofiles
                    ligneprofiles=ligneprofiles[:-1]
                    ##print('['+strssidcount+'] '+ligneprofiles)
                        
                    exec("profile"+strprofiletxtcount+"='"+ligneprofiles+"'")
                    listeprofile.append(ligneprofiles)
                    
                except:
                    pass
                
        fichier1profiles.close()        
        #print('')
        choixprofilverif=False
    except:
        nodatdata=True


def veriflistvide():
    global nodatdata
    global listevide
    global listeprofile
    global valid_btn
    if nodatdata==True:
        listeprofile=["Error, no file !","","Help :","- Go to \"?\"","Click on :","\"générer .DAT\"","go on folder [+]","fill the file",""," ","More help :","reverdyguillaume73","@gmail.com",""]
        valid_btn ['state'] = DISABLED
        valid_btn ['text'] = ' No file found :( '
    elif listeprofile==listevide:
        listeprofile=["Error, no profiles !","","Help :","- Go on folder [+]","fill the file",""," ","More help :","reverdyguillaume73","@gmail.com",""]
        valid_btn ['state'] = DISABLED
        valid_btn ['text'] = ' No profiles save :( '
    else:
        valid_btn ['state'] = NORMAL


def generatemail():
    configpdfprofile()


def tick():
    t = time.strftime('%H:%M:%S')
    label_help.config(text=t)
    label_help.after(200, tick)


def bxl():
    global time1
    time1 = ''
    time2 = time.strftime('%H:%M:%S')      
    if time2 != time1:
        time1 = time2
        label_help.config(text=time2)
        label_help.after(200, bxl)
        tick()
    
###########   ###   ###########

app = Tk()
app.title('Attestation.Py | V 3')
try:
    app.iconbitmap('[+]/ico.ico')
except:
    pass

global var
var = IntVar()
 
def result():
    sprint(var.get())

date = datetime.datetime.now()
day=str(date.day)
month= str(date.month)
year=str(date.year)

    #Centrer fenetre tkinter
screen_x = app.winfo_screenwidth()
screen_y = app.winfo_screenheight()
windows_x = 970
windows_y= 535

posX = (screen_x // 2)- (windows_x //2)
posY = (screen_y // 2)- (windows_y //2)
geo= "{}x{}+{}+{}".format(windows_x, windows_y, posX, posY)

app.geometry(geo)

    #redimensionable = False
app.resizable(width=False, height=False)

    #title
mainframe = LabelFrame(app, text='[By Gugus | reverdyguillaume73@gmail.com]',font=("Russo One","8"), borderwidth='5px',cursor='X_cursor')
mainframe.grid(row=0, column=0, pady=10, padx=20)
label_welcome = Label(mainframe, text="Attestation.Py",font=("Roboto Slab Light","30","bold" ))
label_welcome.grid(row=0, column=0, pady=15, padx=40)

    #title
mainframe1 = LabelFrame(app, text='[Time | '+day+'/'+month+'/'+year+' ]',font=("Russo One","8"), borderwidth='5px',cursor='X_cursor')
mainframe1.grid(row=0, column=1, pady=10, padx=20)

mainframe2 = LabelFrame(mainframe1,font=("Russo One","8"), borderwidth='5px',cursor='X_cursor')
mainframe2.grid(row=0, column=1, pady=10, padx=40)

label_help = Label(mainframe2, text='',font=("Roboto Slab Light","20","bold" ))
label_help.grid(row=0, column=0)
bxl() #pour avoir l'heure

    #listbox
showprofilesframe = LabelFrame(app, text='[All profiles already save]',font=("Comic Sans MS","8","italic" ))
showprofilesframe.grid(row=1, column=0, pady=15, padx=30)
listshowprofiles=Listbox(showprofilesframe, height=5, width=15, borderwidth='2px',cursor='circle', font=("Catamaran Medium","15" ) )
listshowprofiles.grid(row=0, column=0, pady=15, padx=30)

    #scrollbar
scrollbar = Scrollbar(showprofilesframe)
scrollbar.grid(row=0, column=1, sticky="news")

listshowprofiles.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = listshowprofiles.yview)

    #Bouton Radio
radiobuttonframe = LabelFrame(app, text='[Motif]',font=("Comic Sans MS","8","italic" ))
radiobuttonframe.grid(row=1, column=1, pady=15, padx=30)

radio1_widget = Radiobutton(radiobuttonframe, text='1. Travail',variable=var, value=0, font=("Catamaran Medium","12" ), borderwidth='2px',cursor='circle')
radio2_widget = Radiobutton(radiobuttonframe, text='2. Achats',variable=var, value=1, font=("Catamaran Medium","12" ), borderwidth='2px',cursor='circle')
radio3_widget = Radiobutton(radiobuttonframe, text='3. Sante',variable=var, value=2, font=("Catamaran Medium","12" ), borderwidth='2px',cursor='circle')
radio4_widget = Radiobutton(radiobuttonframe, text='4. Famille',variable=var, value=3, font=("Catamaran Medium","12" ), borderwidth='2px',cursor='circle')
radio5_widget = Radiobutton(radiobuttonframe, text='5. Handicap',variable=var, value=4, font=("Catamaran Medium","12" ), borderwidth='2px',cursor='circle')
radio6_widget = Radiobutton(radiobuttonframe, text='6. Sport_Animaux',variable=var, value=5, font=("Catamaran Medium","12" ), borderwidth='2px',cursor='circle')
radio7_widget = Radiobutton(radiobuttonframe, text='7. Convocation',variable=var, value=6, font=("Catamaran Medium","12" ), borderwidth='2px',cursor='circle')
radio8_widget = Radiobutton(radiobuttonframe, text='8. Missions',variable=var, value=7, font=("Catamaran Medium","12" ), borderwidth='2px',cursor='circle')
radio9_widget = Radiobutton(radiobuttonframe, text='9. Enfants',variable=var, value=8, font=("Catamaran Medium","12" ), borderwidth='2px',cursor='circle')

radio1_widget.grid(row=0, column=0, pady=10, padx=15)
radio2_widget.grid(row=0, column=1, pady=10, padx=15)
radio3_widget.grid(row=0, column=2, pady=10, padx=15)

radio4_widget.grid(row=1, column=0, pady=10, padx=15)
radio5_widget.grid(row=1, column=1, pady=10, padx=15)
radio6_widget.grid(row=1, column=2, pady=10, padx=15)

radio7_widget.grid(row=2, column=0, pady=10, padx=15)
radio8_widget.grid(row=2, column=1, pady=10, padx=15)
radio9_widget.grid(row=2, column=2, pady=10, padx=15)


    #Bouton
buttonframe = LabelFrame(app, text='[Send Mail]',font=("Comic Sans MS","8","italic" ))
buttonframe.grid(row=3, column=0, pady=15, padx=30)
valid_btn = Button(buttonframe, text=" SEND ", command=generatemail,font=("Comic Sans MS","12" ), borderwidth='5px',cursor='iron_cross')
valid_btn.grid(row=0, column=0, pady=15, padx=30)

    #Bouton
buttonframehelp = LabelFrame(app, text='[Get help]',font=("Comic Sans MS","8","italic" ))
buttonframehelp.grid(row=3, column=1, pady=15, padx=30)
help_btn = Button(buttonframehelp, text=" ? ", command=centre_daides,font=("Comic Sans MS","12" ), borderwidth='5px',cursor='iron_cross')
help_btn.grid(row=0, column=0, pady=15, padx=30)

showinfotxt()
veriflistvide()
for item in listeprofile:
    listshowprofiles.insert(END, item)

app.mainloop()

##################################
