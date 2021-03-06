# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#

import difflib
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionMajortypeen(Action):

    def name(self) -> Text:
        return "action_major_type_en"
    def run(selfself, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        info = ["it", "computer science", "cs","software engineering","softwareengineering","si","software","computer science","information technologie","informationtechnologie"]
        tel = ["telecom","telecomunication","telecomunications"]
        gc= ["civil engineering", "ce", "civilengineering","civil"]
        em= ["electro", "electro mechanical","electromechanical","em","mechanic","electro mechanic","electromechanic"]
        rti=0
        rtt=0
        rtg=0
        rte=0
        major=tracker.latest_message['text'].split()[-1]
        if (difflib.SequenceMatcher(None,"engineering",major).ratio()>0.8):
            major=tracker.latest_message['text'].split()[-2]


        for i in info:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rti):
                rti=rt
        for t in tel:
            rt=difflib.SequenceMatcher(None,t,major).ratio()
            if(rt>rtt):
                rtt=rt
        for g in gc:
            rt=difflib.SequenceMatcher(None,g,major).ratio()
            if(rt>rtg):
                rtg=rt
        for e in em:
            rt=difflib.SequenceMatcher(None,e,major).ratio()
            if(rt>rte):
                rte=rt
        rts=[str(rti),str(rtt),str(rtg),str(rte)]
        rtmax=max(rts,key=lambda x:float(x))
        msg=""
        if float(rtmax)==rti:
            msg="For the computer science cycle, there are 10 options available: \n" \
                 "-Infini (Financial Computing And Engineering) major\n" \
                 "-DS (Data Science) major\n" \
                 "-Software Architecture Engineering major\n" \
                 "-TwIN (Web And Internet Technologies) major \n" \
                 "-ERP-BI (Enterprise Resource Planning-Business Intelligence) major\n" \
                 "-SIM (Computer And Mobile Systems) major\n" \
                 "-ArcTIC (IT Architecture And Cloud Computing) major\n" \
                 "-SLEAM (Ambient And Mobile Embedded Systems And Software) major\n" \
                 "-NIDS (Network Infrastructure And Data Security) major\n" \
                 "-SE (Software Engineering) major\n" \
                 "You can go to the address https://esprit.tn/formation/ esprit-ingenieur/specialites-et-options" \
                 " for more information"
        if float(rtmax)==rtt:
            msg="For the telecommunications major, there are 2 options available: \n" \
                 "-WIN (Wireless Intelligent Networks) major \n" \
                 "-IoSyS (Internet Of Things Systems & Services) major \n" \
                 "You can go to the address https://esprit.tn/formation/ esprit-ingenieur/specialites-et-options" \
                 "for more information"
        elif float(rtmax)==rtg:
            msg="For the civil engineering major, there are 2 options available: \n "\
                 "-UE Optional O And G (Oil And Gas Engineering) \n" \
                 "-EU Optional Structures And Structures \n " \
                 "You can go to the address https://esprit.tn/formation/ esprit-ingenieur/specialites-et-options" \
                 "for more information"
        elif float(rtmax)==rte:
            msg="For the electromechanical engineering major, there are 2 options available: \n "\
                 "-OGI (Industrial Organization And Management) option \n" \
                 "-Mechatronics option \n" \
                 "You can go to the address https://esprit.tn/formation/ esprit-ingenieur/specialites-et-options" \
                 "for more information"
        if float(rtmax)<0.5:
            msg="Sorry I didn't understand you, you can repeat your question. \n "\
                 "the specialties available are: \n" \
                 "* Computer science \n" \
                 "* Telecommunications \n" \
                 "* Civil engineering \n" \
                 "* Electromechanical engineering"
        dispatcher.utter_message(text=msg)
        return []


class ActionMajorinfoen(Action):

    def name(self) -> Text:
        return "action_major_info_en"
    def run(selfself, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        infini = ["infini","informatique financi??re" , "infomatiquefinanciere"]
        ds = ["ds","data science","data","datascience"]
        sae= ["gl", "sae", "genie logiciel","SoftwareArchitectureEngineering","genie","software"]
        twin= ["twin","web","technologie","Technologies Du Web Et De L???internet"]
        bi=["ERP-BI","erp bi","erp","bi","erpbi","Business Intelligence","Business","Enterprise Resource Planning-Business Intelligence","Enterprise"]
        sim=["mobile","sim","systemes informatiques et mobiles","systemes informatiques et mobiles","systemesinformatiquesetmobiles","systemes"]
        artic=["Architecture IT Et Cloud Computing","ArchitectureITEtCloudComputing","ArchitectureIT","arctic"]
        sleam=["Syst??mes Et Logiciels Embarqu??s Ambiants Et Mobiles","sleam","Embarqu??"]
        nids=["Network Infrastructure And Data Security","Nids","NetworkInfrastructureAndDataSecurity","Network Infrastructure"]
        se=["Software Engineering","SoftwareEngineering","se","infoB"]
        win=["Wireless Intelligent Networks","WirelessIntelligentNetworks","Wireless","win"]
        iosys=["Internet Of Things Systems & Services","internet","iosys","iot"]
        oandg=["Oil And Gas Engineering","OilAndGasEngineering","o and g","oil",'oil and gaz']
        seto=["Structures Et Ouvrages","StructuresEtOuvrages","seto"]
        ogi=["ogi","Organisation Et Gestion Industrielles","organisation"]
        meca=["M??catronique","M??ca","meca"]
        rtinfini=0
        rtds=0
        rtsae=0
        rttwin=0
        rtbi = 0
        rtsim = 0
        rtartic = 0
        rtsleam = 0
        rtnids = 0
        rtse = 0
        rtwin = 0
        rtiosys = 0
        rtoandg = 0
        rtseto = 0
        rtogi = 0
        rtmeca = 0
        text=tracker.latest_message['text'].split()
        start=0
        finish=-1
        count_start=0
        count_finish=0
        check=1
        for i in text:
            check=1
            if(difflib.SequenceMatcher(None,"option",i).ratio()>0.8 or difflib.SequenceMatcher(None, "speciality", i).ratio() >= 0.7 or difflib.SequenceMatcher(None, "the", i).ratio() >= 0.7):

                if(count_start==0):
                    if (difflib.SequenceMatcher(None, "the", i).ratio() >= 0.7):
                        if ((difflib.SequenceMatcher(None,"option",text[text.index(i)+1]).ratio()>0.8 or difflib.SequenceMatcher(None,"speciality",text[text.index(i)+1]).ratio()>0.7)==False):
                            start = text.index(i)
                            count_start = 1
                            check = 0
                    else:
                        start=text.index(i)
                        count_start=1
                        check=0
            if ((difflib.SequenceMatcher(None, "consist", i).ratio() > 0.8 or difflib.SequenceMatcher(None, "of", i).ratio() > 0.8 or difflib.SequenceMatcher(None, "speciality", i).ratio() >= 0.7 or difflib.SequenceMatcher(None, "option", i).ratio() >= 0.7) and count_start==1 and count_finish==0 and check==1):
                finish=text.index(i)
                count_finish=1
        if finish!=-1:
            majorl=text[start+1:finish]
            #major = text[start + 1]
        else:
            majorl=text[start+1:]
        major=""
        for m in majorl:
            major=major+" "+m
        for i in infini:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtinfini):
                rtinfini=rt

        for i in ds:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtds):
                rtds=rt

        for i in sae:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtsae):
                rtsae=rt

        for i in twin:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rttwin):
                rttwin=rt

        for i in bi:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtbi):
                rtbi=rt

        for i in sim:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtsim):
                rtsim=rt

        for i in artic:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtartic):
                rtartic=rt

        for i in sleam:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtsleam):
                rtsleam=rt

        for i in nids:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtnids):
                rtnids=rt

        for i in se:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtse):
                rtse=rt

        for i in win:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtwin):
                rtwin=rt

        for i in iosys:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtiosys):
                rtiosys=rt

        for i in oandg:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtoandg):
                rtoandg=rt

        for i in seto:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtseto):
                rtseto=rt

        for i in ogi:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtogi):
                rtogi=rt

        for i in meca:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtmeca):
                rtmeca=rt

        rts=[str(rtinfini),str(rtds),str(rtsae),str(rttwin),str(rtbi),str(rtsim),str(rtartic),str(rtsleam),str(rtnids),str(rtse),str(rtwin),str(rtiosys),str(rtoandg),str(rtseto),str(rtogi),str(rtmeca)]
        rtmax=max(rts,key=lambda x:float(x))
        msg=""
        if float(rtmax)==rtinfini:
           msg="This major will allow students to apply computer and mathematical tools in the field of finance and insurance."
        if float(rtmax)==rtds:
            msg="The objective of the Data Science option is to acquire a base of knowledge leading to the operational exercise of the profession "\
                 "of a'data scientist'. \n" \
                 "In addition, the objectives of the DS option are: To have a solid knowledge of statistical data processing, To become familiar with the fundamental aspects of Big Data, To master the methods and tools for Artificial Intelligence"
        elif float(rtmax)==rtsae:
            msg="The Software Architecture Engineering major (Ex. GL) is the path of the versatile engineer. A targeted education" \
                 "with complementary axes, in particular in software development, quality, software architectures, data acquisition, tests and validation, systems and networks ... \n" \
                 "This option is dedicated to those looking to succeed in a career as an information systems architect, project manager, IT consultant, developer or even systems and networks specialist."
        elif float(rtmax)==rttwin:
            msg="The objective of the TWIN major is to orient the education of future engineers towards web professions and "\
                 "by strengthening their skills in the following disciplines: \n" \
                 "- Develop proven skills in the most popular web development languages on the job market, \n" \
                 "- Deepen knowledge of development environments, Frameworks and Web best practices, \n" \
                 "- Exploit techniques related to UX user experience and responsive sites, \n" \
                 "- Master the techniques of referencing websites, \n" \
                 "- Master web data analysis techniques: Web Analytics, Data Mining and Big Data."
        elif float(rtmax)==rtbi:
            msg="The ERP-BI major allows students to discover a wide variety of tools, applications and methodologies that "\
                 "allow organizations to collect data. \n" \
                 "This data will then allow analyzes to be set up; \n" \
                 ". Develop and run queries on this data \n" \
                 ". Create reports, dashboards and data visualizations to make analysis results available to decision makers. "
        elif float(rtmax)==rtsim:
            msg="This major makes it possible to train computer engineers specializing in the development of mobile applications "\
                 "on Android and iOS operating systems"
        elif float(rtmax)==rtartic:
            msg="The ArcTIC IT and Cloud Computing Architecture major is a training program for engineering students "\
                 "whose objective is to train engineers capable of: \n" \
                 ". Identify the business needs for cloud infrastructure. \n" \
                 ". Designing enterprise information systems architectures. \n" \
                 ". Ensure the implementation of applications and data storage solutions on servers installed in" \
                 "data centers and their integration into the enterprise system architecture."
        elif float(rtmax)==rtsleam:
            msg="Expertise in the fields of Embedded Computing, Information Systems Engineering, "\
                 "connected objects and mobile applications which are necessary for the design, specification and" \
                 "the prototyping of new on-board, ambient and mobile services. \n" \
                 "A versatile training, with solid multidisciplinary skills around the Internet of Things"
        elif float(rtmax)==rtnids:
            msg="This major allows students to study vulnerabilities in the computer system, design and deploy "\
                 "security solutions according to the latest technologies and regulations."
        elif float(rtmax)==rtse:
            msg="The Software Engineering SE major (Ex. InfoB) aims to train engineers capable of analyzing, "\
                 "to design, develop, test very large computer systems and also to operate" \
                 "innovative and intelligent solutions in the field of software engineering. \n" \
                 "It is on the lookout for the latest technologies and cutting-edge fields of application."
        elif float(rtmax)==rtwin:
            msg="A major (Telecommunication diploma) designed for your professional and personal development. \n" \
                 "A marriage between Data Science and Wireless Communication."
        elif float(rtmax)==rtiosys:
            msg="The IoSyS option trains Telecommunications engineers capable of orchestrating and developing IoT solutions "\
                 "by controlling the entire value chain. \n" \
                 "The IoSyS program is a crossroads of several technologies such as: Big data, machine learning," \
                 "embedded system, web, cloud, Fog, Networks, RFID, WSN, security etc ..."
        elif float(rtmax)==rtoandg:
            msg="The 'Oil and Gas engineering' option will provide our graduates with the fundamental knowledge to undertake " \
                "a career as an entry level engineer in the oil and gas industry or even pursue an advanced " \
                "degree (Master/Ph.D. in Petroleum Engineering). \n" \
                "The option encompasses three (3) core courses that cover the petroleum engineering spectrum from upstream " \
                "perspectives: reservoir engineering, production engineering, and drilling engineering. \n" \
                "The students have the opportunity to contribute to real engineering team projects relevant to the petroleum industry. \n" \
                "National and international experts from the field will offer conferences/training in specific subjects which " \
                "will constitute a core milestone of the students learning process. \n" \
                "Usually, the graduates seek job opportunities with energy producers, Oil services companies, governmental " \
                "institutes, construction companies that offer services to previous companies where they will be involved in " \
                "exploring, discovering appraising, designing facilities/structures, and optimizing production of hydrocarbon assets."
        elif float(rtmax)==rtseto:
            msg="The unit provides students with a set of theoretical and practical knowledge necessary for the design "\
                 "structures and works allowing the mastery of calculation rules and regulatory justifications" \
                 "frames of buildings and special works such as dams, maritime works," \
                 "storage structures (reservoirs, water towers & silos) ...."
        elif float(rtmax)==rtogi:
            msg="The objective of creating the OGI (Industrial Organization and Management) major is to complete and perfect "\
                 "the training of Electromechanical Engineers of Esprit, who wish to have a career in relation with" \
                 "the optimization of performance indicators (KPIs) of a complete supply chain."
        elif float(rtmax)==rtmeca:
            msg="Mechatronics is an industrial process that closely brings together mechanics, electronics, "\
                 "automation and real-time computing, for the design and manufacture of newcomplex and automatic systems.\n" \
                 "The training offered by the Mechatronics option to engineering students in Electromechanics offers a base of" \
                 "solid fundamental knowledge broadening their knowledge through the different facets of this multidisciplinary field" \
                 " and forging links between these different aspects."
        if float(rtmax)<0.5:
            msg="Sorry I didn't understand you, you can repeat your question. \n "\
                 "the available options are:\n" \
                "*Infini\n" \
                "*DS\n" \
                "*SAE\n" \
                "*TWIN\n" \
                "*ERP-BI\n" \
                "*SIM\n" \
                "*ARCTIC\n" \
                "*SLEAM\n" \
                "*NIDS\n" \
                "*SE\n" \
                "*WIN\n" \
                "*IOSYS\n" \
                "*O and G\n" \
                "*Structure et ouvrage\n" \
                "*OGI\n" \
                "*Mecatronique\n"

        dispatcher.utter_message(text=msg)
        return []



class ActionMajortypefr(Action):

    def name(self) -> Text:
        return "action_major_type_fr"
    def run(selfself, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        info = ["info", "informatique", "informatiques"]
        tel = ["telecom","telecomunication","t??l??comunication","telecomunications"]
        gc= ["g??nie civil", "geniecivil", "genie civile","gc"]
        em= ["electro", "electro mecanique","??l??ctro m??canique","em","mecanique"]
        rti=0
        rtt=0
        rtg=0
        rte=0
        major=tracker.latest_message['text'].split()[-1]


        for i in info:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rti):
                rti=rt
        for t in tel:
            rt=difflib.SequenceMatcher(None,t,major).ratio()
            if(rt>rtt):
                rtt=rt
        for g in gc:
            rt=difflib.SequenceMatcher(None,g,major).ratio()
            if(rt>rtg):
                rtg=rt
        for e in em:
            rt=difflib.SequenceMatcher(None,e,major).ratio()
            if(rt>rte):
                rte=rt
        rts=[str(rti),str(rtt),str(rtg),str(rte)]
        rtmax=max(rts,key=lambda x:float(x))
        msg=""
        if float(rtmax)==rti:
            msg="Pour le cyle ing??nieur en informatiques, il exsite 10 options disponibles:\n" \
                "-Option Infini (Informatique Financi??re Et Ing??nierie)\n" \
                "-Option DS (Data Science)\n" \
                "-Option Software Architecture Engineering\n" \
                "-Option TWIN (Technologies Du Web Et De L???INternet)\n" \
                "-Option ERP-BI (Enterprise Resource Planning-Business Intelligence)\n" \
                "-Option SIM (Syst??mes Informatiques Et Mobiles)\n" \
                "-Option ArcTIC (Architecture IT Et Cloud Computing)\n" \
                "-Option SLEAM : (Syst??mes Et Logiciels Embarqu??s Ambiants Et Mobiles)\n" \
                "-Option NIDS (Network Infrastructure And Data Security)\n" \
                "-Option SE (Software Engineering )\n" \
                "Vous pouvez vous rendre sur l'adress https://esprit.tn/formation/esprit-ingenieur/specialites-et-options" \
                " pour plus d'informations"
        if float(rtmax)==rtt:
            msg="Pour le cyle ing??nieur en t??l??communications, il exsite 2 options disponibles:\n" \
                "-Option WIN (Wireless Intelligent Networks)\n" \
                "-Option IoSyS (Internet Of Things Systems & Services)\n" \
                "Vous pouvez vous rendre sur l'adress https://esprit.tn/formation/esprit-ingenieur/specialites-et-options " \
                "pour plus d'informations"
        elif float(rtmax)==rtg:
            msg="Pour le cyle ing??nieur en g??nie civil, il exsite 2 options disponibles:\n" \
                "-UE Optionnelle O And G (Oil And Gas Engineering)\n" \
                "-UE Optionnelle Structures Et Ouvrages\n" \
                "Vous pouvez vous rendre sur l'adress https://esprit.tn/formation/esprit-ingenieur/specialites-et-options " \
                "pour plus d'informations"
        elif float(rtmax)==rte:
            msg="Pour le cycle ing??nieur en genie ??lectromecanique, il exsite 2 options disponibles:\n" \
                "-Option OGI (Organisation Et Gestion Industrielles)\n" \
                "-Option M??catronique\n"\
                "Vous pouvez vous rendre sur l'adress https://esprit.tn/formation/esprit-ingenieur/specialites-et-options " \
                "pour plus d'informations"
        if float(rtmax)<0.5:
            msg="D??sole je ne vous ai pas compris, vous pouvez r??peter votre question.\n" \
                "les sp??cialit??s disponibles sont :\n" \
                "*Informatique\n" \
                "*T??l??communications\n" \
                "*G??nie civil\n" \
                "*Genie el??crom??canique"
        dispatcher.utter_message(text=msg)
        return []



class ActionMajorinfofr(Action):

    def name(self) -> Text:
        return "action_major_info_fr"
    def run(selfself, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        infini = ["infini","informatique financi??re" , "infomatiquefinanciere"]
        ds = ["ds","data science","data","datascience"]
        sae= ["gl", "sae", "genie logiciel","SoftwareArchitectureEngineering","genie","software"]
        twin= ["twin","web","technologie","Technologies Du Web Et De L???internet"]
        bi=["ERP-BI","erp bi","erp","bi","erpbi","Business Intelligence","Business","Enterprise Resource Planning-Business Intelligence","Enterprise"]
        sim=["mobile","sim","systemes informatiques et mobiles","systemes informatiques et mobiles","systemesinformatiquesetmobiles","systemes"]
        artic=["Architecture IT Et Cloud Computing","ArchitectureITEtCloudComputing","ArchitectureIT","arctic"]
        sleam=["Syst??mes Et Logiciels Embarqu??s Ambiants Et Mobiles","sleam","Embarqu??"]
        nids=["Network Infrastructure And Data Security","Nids","NetworkInfrastructureAndDataSecurity","Network Infrastructure"]
        se=["Software Engineering","SoftwareEngineering","se","infoB"]
        win=["Wireless Intelligent Networks","WirelessIntelligentNetworks","Wireless","win"]
        iosys=["Internet Of Things Systems & Services","internet","iosys","iot"]
        oandg=["Oil And Gas Engineering","OilAndGasEngineering","o and g","oil",'oil and gaz']
        seto=["Structures Et Ouvrages","StructuresEtOuvrages","seto"]
        ogi=["ogi","Organisation Et Gestion Industrielles","organisation"]
        meca=["M??catronique","M??ca","meca"]
        rtinfini=0
        rtds=0
        rtsae=0
        rttwin=0
        rtbi = 0
        rtsim = 0
        rtartic = 0
        rtsleam = 0
        rtnids = 0
        rtse = 0
        rtwin = 0
        rtiosys = 0
        rtoandg = 0
        rtseto = 0
        rtogi = 0
        rtmeca = 0
        text=tracker.latest_message['text'].split()
        start=0
        finish=-1
        count_start=0
        count_finish=0
        check=1
        for i in text:
            check=1
            if(difflib.SequenceMatcher(None,"option",i).ratio()>0.8 or difflib.SequenceMatcher(None, "specialite", i).ratio() >= 0.7):
                if(count_start==0):
                    start=text.index(i)
                    count_start=1
                    check=0
            if ((difflib.SequenceMatcher(None, "consiste", i).ratio() > 0.8 or difflib.SequenceMatcher(None, "de", i).ratio() > 0.8 or difflib.SequenceMatcher(None, "specialite", i).ratio() >= 0.7) and count_start==1 and count_finish==0 and check==1):
                finish=text.index(i)
                count_finish=1
        if finish!=-1:
            majorl=text[start+1:finish]
            #major = text[start + 1]
        else:
            majorl=text[start+1:]
        major=""
        for m in majorl:
            major=major+" "+m
        for i in infini:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtinfini):
                rtinfini=rt

        for i in ds:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtds):
                rtds=rt

        for i in sae:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtsae):
                rtsae=rt

        for i in twin:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rttwin):
                rttwin=rt

        for i in bi:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtbi):
                rtbi=rt

        for i in sim:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtsim):
                rtsim=rt

        for i in artic:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtartic):
                rtartic=rt

        for i in sleam:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtsleam):
                rtsleam=rt

        for i in nids:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtnids):
                rtnids=rt

        for i in se:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtse):
                rtse=rt

        for i in win:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtwin):
                rtwin=rt

        for i in iosys:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtiosys):
                rtiosys=rt

        for i in oandg:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtoandg):
                rtoandg=rt

        for i in seto:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtseto):
                rtseto=rt

        for i in ogi:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtogi):
                rtogi=rt

        for i in meca:
            rt=difflib.SequenceMatcher(None,i,major).ratio()
            if(rt>rtmeca):
                rtmeca=rt

        rts=[str(rtinfini),str(rtds),str(rtsae),str(rttwin),str(rtbi),str(rtsim),str(rtartic),str(rtsleam),str(rtnids),str(rtse),str(rtwin),str(rtiosys),str(rtoandg),str(rtseto),str(rtogi),str(rtmeca)]
        rtmax=max(rts,key=lambda x:float(x))
        msg=""
        if float(rtmax)==rtinfini:
           msg="Cette option va permettre aux ??tudiants d'appliquer les outils informatiques et math??matiques dans le domaine de la finance et l'assurance."
        if float(rtmax)==rtds:
            msg="L'objectif de l'option Data Science est d'acqu??rir un socle de connaissances conduisant ?? l'exercice op??rationnel du m??tier" \
                " de ??datascientist??. \n" \
                "Par ailleurs, les objectifs de l'option DS sont: Avoir une solide connaissance en traitement statistique des donn??es, Se familiariser avec les aspects fondamentaux du Big Data, Ma??triser les m??thodes et les outils pour l'Intelligence Artificielle"
        elif float(rtmax)==rtsae:
            msg="L'option Software Architecture Engineering (Ex. GL) est les chemain de l'ing??nieur polyvalent. Une formation" \
                " cibl??e et ?? axes compl??mentaires notamment en d??veloppement de logiciels, qualit??, architectures logicielles, acquisition des donn??es, tests et validation, syst??mes et r??seaux...\n" \
                " Cette option est d??di??e ?? ceux qui cherchent ?? r??ussir une carri??re d'architecte en syst??mes d'information, de chef de projet, de consultant IT, de d??veloppeur ou m??me de sp??cialiste syst??mes et reseaux."
        elif float(rtmax)==rttwin:
            msg="L'objectif de l'option TWIN est d???orienter la formation des futurs ing??nieurs vers les m??tiers du web et " \
                "de l???internet en renfor??ant leurs comp??tences dans les disciplines suivantes: \n" \
                "??? D??velopper des comp??tences confirm??es dans les langages de d??veloppement Web les plus r??pandues sur le march?? de travail, \n" \
                "??? Approfondir les connaissances des environnements de d??veloppement, des Frameworks et des bonnes pratiques du Web, \n" \
                "??? Exploiter les techniques li??es ?? l???exp??rience utilisateur UX et des sites responsives, \n" \
                "??? Maitriser les techniques de r??f??rencement des sites web, \n" \
                "??? Maitriser les techniques d???analyse des donn??es du web: Web Analytics, Data Mining et Big Data."
        elif float(rtmax)==rtbi:
            msg="L'option ERP-BI permet aux ??tudiants de d??couvrir une grande vari??t?? d'outils, d'applications et de m??thodologies qui " \
                "permettent aux organisations de collecter des donn??es. \n" \
                "Ces donn??es permettront par la suite de mettre en place des analyses ; \n" \
                ". D??velopper et ex??cuter des requ??tes sur ces donn??es \n" \
                ". Cr??er des rapports, des tableaux de bord et des visualisations de donn??es pour mettre les r??sultats d'analyse ?? la disposition des d??cideurs."
        elif float(rtmax)==rtsim:
            msg="Cette option permet de former des ing??nieurs en informatique sp??cialis??s dans le d??veloppement des applications mobile " \
                "sur les syst??mes d'exploitation Android et iOS"
        elif float(rtmax)==rtartic:
            msg="L???option Architecture IT et Cloud Computing ArcTIC est un programme de formation pour les ??l??ves ing??nieurs " \
                "dont l???objectif est de former des ing??nieurs capable de : \n" \
                ". Identifier les besoins de l???entreprise en mati??re d???infrastructures d??mat??rialis??es. \n" \
                ". Concevoir des architectures de syst??mes d???information des entreprises. \n" \
                ". Assurer la mise en place d???applications et de solutions de stockage de donn??es sur des serveurs install??s dans des " \
                "data centers et leur int??gration dans l???architecture syst??me de l???entreprise."
        elif float(rtmax)==rtsleam:
            msg="Une expertise dans les domaines de l???Informatique embarqu??e, l???Ing??nierie des syst??mes d???Information , " \
                "les objets connect??s et les applications mobiles qui sont n??cessaires ?? la conception, la sp??cification et " \
                "le prototypage de nouveaux services embarqu??s, ambiants et mobiles. \n" \
                "Une formation polyvalente, avec de solides comp??tences pluridisciplinaires autour de l'internet des objets"
        elif float(rtmax)==rtnids:
            msg="Cette option permet aux ??tudiants d'??tudier les failles du syst??me informatique, concevoir et d??ployer des " \
                "solutions de s??curit?? en fonction des derni??res technologies et des r??glementations."
        elif float(rtmax)==rtse:
            msg="L'option Software Engineering SE (Ex. InfoB) a pour vocation de former des ing??nieurs capable d???analyser, " \
                "concevoir, d??velopper, tester des syst??mes informatiques de tr??s grande envergure et aussi d'exploiter des " \
                "solutions innovantes et intelligentes dans le domaine d'ing??nierie logicielle . \n" \
                "Il est ?? l'aff??t des plus r??centes technologies et des domaines d'application de pointe."
        elif float(rtmax)==rtwin:
            msg="Une option (dipl??me de T??l??communication) con??ue pour votre ??panouissement professionnel et personnel. \n" \
                "Un mariage entre le Data Science et les Wireless Communication."
        elif float(rtmax)==rtiosys:
            msg="L???option IoSyS forme des ing??nieurs T??l??communications capables d???orchestrer et de d??velopper des solutions " \
                "IoT en ma??trisant toute la cha??ne de valeur. \n" \
                "Le programme IoSyS est un carrefour de plusieurs technologies comme: Big data, machine Learning, " \
                "syst??me embarqu??, web, cloud, Fog, R??seaux, RFID, WSN, s??curit?? etc???"
        elif float(rtmax)==rtoandg:
            msg="L'option 'Ing??nierie p??troli??re et gazi??re' fournira ?? nos dipl??m??s les connaissances fondamentales " \
                "n??cessaires pour entreprendre une carri??re d'ing??nieur d??butant dans l'industrie p??troli??re et gazi??re ou m??me " \
                "poursuivre un dipl??me d'??tudes sup??rieures (Master/Ph.D. in Petroleum Engineering). \n" \
                "L'option comprend trois (3) cours de base qui couvrent le spectre de l'ing??nierie p??troli??re du point " \
                "de vue amont: ing??nierie de r??servoir, ing??nierie de production et ing??nierie de forage. \n" \
                "Les ??tudiants ont la possibilit?? de contribuer ?? de v??ritables projets d'??quipe d'ing??nierie pertinents pour " \
                "l'industrie p??troli??re. \n" \
                "Des experts nationaux et internationaux du domaine offriront des conf??rences / formations sur des sujets " \
                "sp??cifiques qui constitueront une ??tape cl?? du processus d'apprentissage des ??tudiants.\n" \
                "Habituellement, les dipl??m??s recherchent des opportunit??s d'emploi avec des producteurs d'??nergie, " \
                "des soci??t??s de services p??troliers, des instituts gouvernementaux, des entreprises de construction qui " \
                "offrent des services aux entreprises pr??c??dentes o?? ils seront impliqu??s dans l'exploration, la d??couverte, " \
                "l'??valuation, la conception d'installations installations/structures et l'optimisation de la production des actifs d'hydrocarbures."
        elif float(rtmax)==rtseto:
            msg="L???unit?? procure aux ??tudiants un ensemble de connaissances th??oriques et pratiques n??cessaires ?? la conception " \
                "des structures et des ouvrages permettant la ma??trise des r??gles de calcul et des justifications r??glementaires " \
                "des ossatures de b??timents et des ouvrages particuliers tels que les barrages, les ouvrages maritimes, " \
                "les ouvrages de stockage (r??servoirs, ch??teaux d???eau & silos)...."
        elif float(rtmax)==rtogi:
            msg="L???objectif de la cr??ation de l???option OGI (Organisation et Gestion Industrielles) est de compl??ter et parfaire " \
                "la formation des Ing??nieurs Electrom??caniciens d???Esprit, qui souhaitent avoir une carri??re en relation avec " \
                "l???optimisation des indicateurs de performance (KPI) d???une chaine logistique compl??te."
        elif float(rtmax)==rtmeca:
            msg="La M??catronique est une d??marche industrielle qui rassemble ??troitement la m??canique, l?????lectronique, " \
                "l???automatique et l???informatique temps r??el, pour la conception et la fabrication de nouveaux syst??mes " \
                "automatiques complexe. \n" \
                "La formation qu???offre l???option M??catronique aux ??l??ves ing??nieurs en Electrom??canique, propose un socle de " \
                "connaissances fondamentales solides ??largissant leurs savoir par les diff??rentes facettes de ce domaine " \
                "pluridisciplinaire et tissant des liens entre ces diff??rents aspects."
        if float(rtmax)<0.5:
            msg="D??sole je ne vous ai pas compris, vous pouvez r??peter votre question.\n" \
                "les options disponibles sont :\n" \
                "*Infini\n" \
                "*DS\n" \
                "*SAE\n" \
                "*TWIN\n" \
                "*ERP-BI\n" \
                "*SIM\n" \
                "*ARCTIC\n" \
                "*SLEAM\n" \
                "*NIDS\n" \
                "*SE\n" \
                "*WIN\n" \
                "*IOSYS\n" \
                "*O and G\n" \
                "*Structure et ouvrage\n" \
                "*OGI\n" \
                "*M??catronique\n"

        dispatcher.utter_message(text=msg)
        return []