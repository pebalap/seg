import requests
from bs4 import BeautifulSoup
from googlesearch import search
from termcolor import colored
import os
import random
import time
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_ascii(title):
    if title == "Cyber Toolkit":
        print(colored("""
                                      ####################
                               ##############++--++##############
                          #########--------------------------#########
                       #######----------------++#+----------------#######
                    ######--------+###-------+-####------####--------+######
                 ######-----------+####-------##-#-------+###-----------+######
               ######--------------#+#----------+----------+------++##-----######
             #####+------####+-------#----------+#-------+---------+###------#####
            ####+------#++###+----------------+#-+-------#---------####+#------#####
          #####--------#+##+-----------##++-#+---+--+##--#+-----+----##+#--------#####
         ####----------##+##----##-----########+++--+####+---##-----##+##----------####
        ####--------------++#+--#+##------#-#############----+#---+#++--------------####
      ####------------------###-+-----------#-################---###-----------------####
     ####--------------------+#++-+#----------#+--#+#########-++##+-------------------+###
     ###-----------------------###+---####---++--------####+--###----------------------+###
    ###-------------------------+#+#+##################++++++-++------------------------+###
   ####--------------------------+######################++-+-+---------------------------####
  ####--------------------------+########################++++-----------------------------###
  ###---------------------------########################++++++-+--------------------------+###
  ###---------------------#####+#######################++##+--+++#####---------------------###
 ###+++++++++++++++++++++++##++##+++######################+----++++##+++++++++++++++++++++++###
 ###+++++++++++++++++++++++++++###--######################+---+#++++++++++++++++++++++++++++###
 ###+++++++++++++++++++++++++++###-###------######++----##++--++++++++++++++++++++++++++++++###
###+++++++++++++++++++++++++++++###+--------+#+#+--------------+++++++++++++++++++++++++++++###
################################+##+#++-----+###-+---------------##############################
################################++#++#+---++####+++------+#+++---##############################
####################################----++#####--++#+-++---+-+--+##############################
##############################################----#+++####---++-###############################
 ###-----------------------------+-###########----+---#####---------------------------------###
 ###-###-------------------------+++#-+######+---------##+----------------------------------###
 ###---#---------------------------+##-#########-------#+------------------------------####-###
  ##-####------------------------#####+###########+-####---+###------------------------###-###
  ###-###-----------------------###################+------++####+----------------------+-+-###
  ####-+----------------------####+-####+##########-----+++--+####--------------------###-####
   ###-+###------------------####----##############+-+-++------####------------------#+#-+###
   ####-###-----------------###------##############+##+#-+-------+##+---------------####-###
    ####-###+-------------+#+--------###################-----------+#+-------------####-####
     ####-##----------------------------###############--------------------------------####
      ####-##+#----------------------------######+#+-----------------------------####-####
       ####-+-##---------------------------------------------------------------##-##-####
        ####+##-##------------------------------------------------------------#-##-#####
         #####-####---------------------------------------------------------####+-####
           #####--#-++----------------------------------------------------###+--#####
             #####-#####------------------------------------------------+#-#--#####
              ######-#####------------------------------------------+##---#-#####
                 #####-####-##+-----------------------------------##-###-+#####
                   ######--##-###---------------------------+#-##+###--######
                     ########-###########--+---------##-###+##-#++-########
                        #########----####--##+#+#+##+###-##----########
                            ############-------+--+-----############
                                  ############################

                                       (CODE BY KADEZ-406)
                                  #THANKS FOR SUDATTACK CYBER TEAM
                                  #THAKS FOR CYBER SEDERHANA TEAM
                           ~this tools made by kadez-406 from {S.A.C.T~CST}~
        """, 'green'))
    elif title == "Single Site Check":
        print(colored("""
███████╗██╗███╗   ██╗ ██████╗ ██╗     ███████╗    ███████╗██╗████████╗███████╗
██╔════╝██║████╗  ██║██╔════╝ ██║     ██╔════╝    ██╔════╝██║╚══██╔══╝██╔════╝
███████╗██║██╔██╗ ██║██║  ███╗██║     █████╗      ███████╗██║   ██║   █████╗
╚════██║██║██║╚██╗██║██║   ██║██║     ██╔══╝      ╚════██║██║   ██║   ██╔══╝
███████║██║██║ ╚████║╚██████╔╝███████╗███████╗    ███████║██║   ██║   ███████╗
╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝    ╚══════╝╚═╝   ╚═╝   ╚══════╝

        """, 'cyan'))
    elif title == "Mass Site Check":
        print(colored("""
███╗   ███╗ █████╗ ███████╗███████╗    ███████╗██╗████████╗███████╗
████╗ ████║██╔══██╗██╔════╝██╔════╝    ██╔════╝██║╚══██╔══╝██╔════╝
██╔████╔██║███████║███████╗███████╗    ███████╗██║   ██║   █████╗
██║╚██╔╝██║██╔══██║╚════██║╚════██║    ╚════██║██║   ██║   ██╔══╝
██║ ╚═╝ ██║██║  ██║███████║███████║    ███████║██║   ██║   ███████╗
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚══════╝╚═╝   ╚═╝   ╚══════╝

        """, 'cyan'))
    elif title == "Check with Dork":
        print(colored("""
██████╗  ██████╗ ██████╗ ██╗  ██╗    ███████╗██╗████████╗███████╗
██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝    ██╔════╝██║╚══██╔══╝██╔════╝
██║  ██║██║   ██║██████╔╝█████╔╝     ███████╗██║   ██║   █████╗
██║  ██║██║   ██║██╔══██╗██╔═██╗     ╚════██║██║   ██║   ██╔══╝
██████╔╝╚██████╔╝██║  ██║██║  ██╗    ███████║██║   ██║   ███████╗
╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚══════╝╚═╝   ╚═╝   ╚══════╝


        """, 'cyan'))
    elif title == "Mood Booster":
        print(colored("""
███╗   ███╗ ██████╗  ██████╗ ██████╗
████╗ ████║██╔═══██╗██╔═══██╗██╔══██╗
██╔████╔██║██║   ██║██║   ██║██║  ██║
██║╚██╔╝██║██║   ██║██║   ██║██║  ██║
██║ ╚═╝ ██║╚██████╔╝╚██████╔╝██████╔╝
╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═════╝


        """, 'cyan'))

def single_site_check(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(colored("[+]", 'white'), colored(url, 'white'), colored("[VULN]", 'green'))
            with open("vuln.txt", "a") as file:
                file.write(url + "\n")
        else:
            print(colored("[+]", 'white'), colored(url, 'white'), colored("[NOT VULN]", 'red'))
            with open("not.txt", "a") as file:
                file.write(url + "\n")
    except Exception as e:
        print(colored(f"Request failed: {e}", 'red'))

def mass_site_check(file_path):
    try:
        with open(file_path, "r") as file:
            urls = file.readlines()
            for url in urls:
                single_site_check(url.strip())
    except Exception as e:
        print(colored(f"Error reading file: {e}", 'red'))

def check_with_dork(dork):
    try:
        for url in search(dork, stop=20):
            single_site_check(url)
    except Exception as e:
        print(colored(f"Search failed: {e}", 'red'))

quotes = {
    "Senang": [
        "Kebahagiaan bukanlah sesuatu yang dibuat siap jadi. Itu berasal dari tindakan Anda sendiri. Senangkan dirimu dengan apa yang kamu miliki; bersukacitalah dengan cara-cara yang kamu jalani. Kebahagiaan bukanlah tujuan. Itu adalah produk sampingan dari hidup dengan baik.",
        "Ketika kamu senang, kamu menikmati musik. Ketika kamu sedih, kamu memahami lirik. Jangan mencari kebahagiaan, ciptakanlah. Kebahagiaan adalah seni untuk tidak pernah mengingat apa yang buruk telah terjadi.",
        "Senyum adalah cara termudah untuk memperbaiki penampilanmu. Kebahagiaan adalah keputusan, bukan kondisi. Jadi, buatlah keputusan untuk bahagia setiap hari.",
        "Hidup adalah tentang menemukan kebahagiaan dalam perjalanan, bukan hanya pada tujuan. Jadi, nikmati setiap langkah yang kamu ambil."
    ],
    "Sedih": [
        "Kesedihan adalah bagian dari hidup, tetapi itu bukanlah hidupmu sepenuhnya. Biarkan air mata membersihkan jalan untuk kebahagiaan di masa depan. Tidak apa-apa untuk merasa sedih. Itu adalah bagian dari menjadi manusia.",
        "Kesedihan bisa menjadi jembatan menuju kedamaian. Setiap air mata mengajarkan pelajaran yang tak ternilai. Kesedihan adalah cara hati memberi tahu bahwa ia sedang menyembuhkan.",
        "Kesedihan bukanlah kelemahan, itu adalah kekuatan yang belum terungkap. Berikan waktu untuk dirimu sendiri untuk merasakan dan sembuh. Jangan pernah meremehkan kekuatan istirahat dan refleksi diri.",
        "Ketika kamu merasa sedih, ingatlah bahwa setelah hujan selalu ada pelangi. Teruslah berjuang dan percayalah bahwa hari yang lebih baik akan datang."
    ],
    "Stres": [
        "Ambil napas dalam-dalam. Kamu lebih kuat daripada yang kamu pikirkan. Stres adalah bagian dari hidup. Hadapi dengan tenang dan perlahan. Jangan biarkan stres mengendalikanmu. Alihkan fokusmu pada hal-hal positif.",
        "Ingatlah untuk selalu menjaga kesehatan mentalmu. Tidak apa-apa untuk istirahat. Setiap masalah pasti ada solusinya. Jangan biarkan stres menghalangimu untuk melihatnya. Tenangkan pikiranmu dan segarkan jiwamu.",
        "Jangan takut untuk meminta bantuan ketika stres terasa terlalu berat. Hidup adalah perjalanan, bukan perlombaan. Nikmati setiap langkah yang kamu ambil dan berikan dirimu penghargaan untuk setiap pencapaian.",
        "Stres adalah bagian dari proses pertumbuhan. Hadapilah dengan kepala tegak dan hati yang tenang, dan kamu akan menjadi pribadi yang lebih kuat."
    ],
    "Lelah": [
        "Istirahatlah. Tidak ada gunanya terus bergerak tanpa henti. Kegigihan Anda adalah kunci kesuksesan, tetapi jangan lupakan pentingnya istirahat. Setiap langkah menuju kesuksesan membutuhkan istirahat. Jaga keseimbangan Anda.",
        "Jangan pernah meremehkan kekuatan tidur yang cukup. Itu adalah bahan bakar untuk kesuksesan Anda. Hidup adalah tentang menemukan keseimbangan antara bekerja keras dan beristirahat.",
        "Lelah adalah tanda bahwa kamu sedang bekerja menuju sesuatu yang berarti. Ambil waktu untuk beristirahat dan pulihkan energi. Jangan terlalu keras pada diri sendiri. Tubuhmu juga butuh istirahat.",
        "Ketika tubuhmu lelah, berikanlah waktu untuk pulih. Ingatlah bahwa menjaga kesehatan fisik dan mental adalah kunci untuk mencapai tujuanmu dengan baik."
    ],
    "Gelisah": [
        "Cobalah untuk fokus pada hal-hal yang dapat Anda kendalikan, dan biarkan yang lainnya berjalan dengan alirannya. Lakukan beberapa latihan pernapasan atau meditasi untuk menenangkan pikiran Anda.",
        "Jangan terjebak dalam pikiran negatif. Fokus pada solusi, bukan masalahnya. Hidup adalah tentang perjalanan, bukan tujuan. Nikmati setiap langkahnya.",
        "Masa lalu adalah pelajaran, masa depan adalah kesempatan. Hiduplah di saat ini. Gelisah adalah tanda bahwa kamu sedang bergerak keluar dari zona nyamanmu.",
        "Hadapi ketakutanmu dengan keberanian, bukan dengan rasa gelisah. Jangan biarkan kekhawatiran menghancurkan hari yang indah. Ingatlah bahwa setiap tantangan adalah kesempatan untuk berkembang."
    ],
    "Bahagia": [
        "Selamat! Pertahankan sikap positif Anda dan bagikan kebahagiaan kepada orang lain di sekitar Anda. Teruskan hal-hal yang membuat Anda bahagia dan bersyukur atas semua berkah yang Anda miliki.",
        "Ketika Anda merasa bahagia, luangkan waktu untuk bersyukur. Kebahagiaan adalah anugerah. Berikan kebahagiaan kepada orang lain, dan kebahagiaan akan kembali kepada Anda.",
        "Hidup adalah tentang memberi dan menerima kebahagiaan. Bagikan senyum Anda kepada dunia. Kebahagiaan adalah keadaan pikiran. Tetaplah positif dan nikmati setiap momen.",
        "Bagikan kebahagiaanmu dan lihat dunia berubah menjadi tempat yang lebih baik. Bersyukur adalah kunci kebahagiaan sejati. Jadi, jadilah pribadi yang selalu bersyukur dalam setiap situasi."
    ]
}

religious_quotes = {
    "Al-Quran": [
        "Dan carilah pada apa yang telah dianugerahkan Allah kepadamu (kebahagiaan) negeri akhirat, dan janganlah kamu melupakan bagianmu dari (kenikmatan) duniawi dan berbuat baiklah (kepada orang lain) sebagaimana Allah telah berbuat baik kepadamu, dan janganlah kamu berbuat kerusakan di (muka) bumi. Sesungguhnya Allah tidak menyukai orang-orang yang berbuat kerusakan. (QS. Al-Qasas: 77)",
        "Allah tidak membebani seseorang melainkan sesuai dengan kesanggupannya. (QS. Al-Baqarah: 286)",
        "Dan sungguh, Kami telah menciptakan manusia dan mengetahui apa yang dibisikkan oleh hatinya, dan Kami lebih dekat kepadanya daripada urat lehernya. (QS. Qaf: 16)",
        "Dan barangsiapa bertawakkal kepada Allah niscaya Allah akan mencukupkan (keperluannya). Sesungguhnya Allah melaksanakan urusan yang (dikehendaki)Nya. Sesungguhnya Allah telah mengadakan ketentuan bagi tiap-tiap sesuatu. (QS. At-Talaq: 3)"
    ],
    "Alkitab": [
        "Segala perkara dapat kutanggung di dalam Dia yang memberi kekuatan kepadaku. (Filipi 4:13)",
        "Tuhan adalah gembalaku, takkan kekurangan aku. (Mazmur 23:1)",
        "Janganlah kamu khawatir tentang apapun juga, tetapi nyatakanlah dalam segala hal keinginanmu kepada Allah dalam doa dan permohonan dengan ucapan syukur. (Filipi 4:6)",
        "Kasih itu sabar; kasih itu murah hati; ia tidak cemburu. Ia tidak memegahkan diri dan tidak sombong. (1 Korintus 13:4)"
    ],
    "Tripitaka": [
        "Kebencian tidak akan pernah berakhir jika kebencian dibalas dengan kebencian; Kebencian berakhir dengan cinta. Ini adalah hukum yang abadi. (Dhammapada 1:5)",
        "Janganlah engkau mencari perlindungan pada orang lain, berusahalah untuk menjadi pelindung bagi dirimu sendiri. (Dhammapada 25:236)",
        "Kemenangan melahirkan permusuhan, yang kalah hidup dalam kesedihan. Mereka yang damai hidup bahagia, meninggalkan kemenangan dan kekalahan. (Dhammapada 15:201)",
        "Jangan meremehkan perbuatan baik meskipun kecil; setetes demi setetes, guci akan penuh. (Dhammapada 9:122)"
    ],
    "Veda": [
        "Kebenaran itu satu, hanya orang bijak menyebutnya dengan berbagai nama. (Rigveda 1.164.46)",
        "Semoga semua makhluk di semua dunia menjadi bahagia. (Yajurveda 36.17)",
        "Manusia yang baik bukanlah manusia yang tidak pernah gagal, tetapi manusia yang selalu bangkit kembali setelah kejatuhan. (Atharvaveda 12.2.31)",
        "Penyembahan terhadap yang ilahi harus dilakukan dengan hati yang penuh kasih sayang, bukan dengan ritual yang kaku. (Bhagavad Gita 9:26)"
    ],
    "Motivasi": [
        "Jangan menunggu waktu yang sempurna untuk mulai, karena waktu yang sempurna tidak akan pernah datang. Mulailah sekarang dan gunakan waktu yang Anda miliki. - Napoleon Hill",
        "Orang-orang yang cukup gila untuk berpikir mereka dapat mengubah dunia adalah orang-orang yang melakukannya. - Steve Jobs",
        "Kesuksesan tidak selalu tentang bakat, tapi tentang ketekunan dan kerja keras. - J.K. Rowling",
        "Jangan takut untuk gagal, karena kegagalan adalah langkah menuju kesuksesan. - Michael Jordan"
    ],
    "Bingung": [
        "Kadang-kadang kita harus tersesat untuk menemukan jalan kita. - David Steindl-Rast",
        "Kebingungan adalah awal dari kebijaksanaan. - Aristotle",
        "Kita hanya memahami sepenuhnya hidup setelah kita menerima kebingungan sebagai bagian dari itu. - Carl Jung",
        "Dalam kebingungan, ada potensi untuk menemukan diri sejati kita. - Bruce Lee"
    ],
    "Harapan": [
        "Harapan adalah satu-satunya hal yang lebih kuat dari ketakutan. - Suzanne Collins",
        "Harapan adalah mimpi dari seorang yang terjaga. - Aristotle",
        "Harapan adalah kekuatan untuk mempercayai bahwa hari esok bisa menjadi lebih baik daripada hari ini. - Zig Ziglar",
        "Di tengah-tengah kesulitan terdapat kesempatan. - Albert Einstein"
    ],
    "Kesabaran": [
        "Kesabaran adalah pendamping kebijaksanaan. - Saint Augustine",
        "Sabar adalah kekuatan. Ketidaksabaran adalah kelemahan. - Bruce Lee",
        "Dengan kesabaran, segala sesuatu yang sulit menjadi mudah. - Saadi",
        "Kesabaran adalah kemampuan untuk menunggu dengan sikap baik. - Joyce Meyer"
    ],
    "Rasa Syukur": [
        "Rasa syukur adalah pintu menuju kebahagiaan. - Buddha",
        "Tidak ada yang lebih indah daripada bersyukur pada hari ini. - Thich Nhat Hanh",
        "Bersyukur membuat kita lebih bahagia dan sehat. - Cicero",
        "Rasa syukur mengubah apa yang kita miliki menjadi cukup. - Melody Beattie"
    ]
}

mood_examples = {
    "Senang": ["Senang", "Gembira", "Bahagia", "Ceria", "Suka"],
    "Sedih": ["Sedih", "Kecewa", "Gundah", "Galau", "Patah hati"],
    "Stres": ["Stres", "Cemas", "Gelisah", "Panas", "Takut"],
    "Lelah": ["Lelah", "Capek", "Penghabisan", "Kelelahan", "Lesu"],
    "Gelisah": ["Gelisah", "Was-was", "Gugup", "Cemas", "Kuatir"],
    "Bahagia": ["Bahagia", "Senang", "Suka", "Gembira", "Girang"],
    "Al-Quran": ["Islam", "Muslim", "Al-Quran", "Quran", "Qur'an"],
    "Alkitab": ["Kristen", "Nasrani", "Injil", "Bible", "Alkitab"],
    "Tripitaka": ["Buddha", "Buddhisme", "Tripitaka", "Dhammapada"],
    "Veda": ["Hindu", "Hinduisme", "Veda", "Bhagavad Gita"]
}

def get_random_quote(mood):
    if mood.capitalize() in quotes:
        return random.choice(quotes[mood.capitalize()])
    elif mood.capitalize() in religious_quotes:
        return random.choice(religious_quotes[mood.capitalize()])
    else:
        return "Maaf, kutipan untuk mood ini tidak tersedia. Silakan pilih mood lain."

def display_mood_examples():
    print("Masukkan kondisi mood Anda (contoh):")
    for mood, examples in mood_examples.items():
        print(f"{mood}: {', '.join(examples)}")

def mood_booster():
    while True:
        mood = input(f"Masukkan kondisi mood Anda ({', '.join(quotes.keys())} atau ketik 'help' untuk contoh): ")
        if mood.lower() == 'help':
            print("Contoh mood yang dapat dimasukkan: Senang, Sedih, Stres, Lelah, Gelisah, Motivasi, Bingung, Harapan, Kesabaran, Rasa Syukur")
            print(mood_examples)
        else:
            quote = get_random_quote(mood)
            print(colored(f"Quote untuk mood {mood}:", 'cyan'))
            print(colored(quote, 'yellow'))
            break
    input("Tekan Enter untuk kembali ke menu...")

def exit_toolkit():
    print(colored("Keluar dari Cyber Toolkit. Sampai jumpa!", 'green'))
    sys.exit()

def main_menu():
    clear_screen()
    display_ascii("Cyber Toolkit")
    print(colored("Pilih fitur:", 'yellow'))
    print(colored("1. Single Site Check", 'red'))
    print(colored("2. Mass Site Check", 'blue'))
    print(colored("3. Check with Dork", 'yellow'))
    print(colored("4. Mood Booster", 'white'))
    print(colored("5. Generate SQLMap Command", 'green'))
    print(colored("6. exit", 'cyan'))
    choice = input("Masukkan pilihan Anda (1/2/3/4/5/0): ")

    if choice == '1':
        clear_screen()
        display_ascii("Single Site Check")
        url = input("Masukkan URL: ")
        single_site_check(url)
        input("\nTekan Enter untuk kembali ke menu...")
    elif choice == '2':
        clear_screen()
        display_ascii("Mass Site Check")
        file_path = input("Masukkan path file: ")
        mass_site_check(file_path)
        input("\nTekan Enter untuk kembali ke menu...")
    elif choice == '3':
        clear_screen()
        display_ascii("Check with Dork")
        dork = input("Masukkan Dork: ")
        dork_search(dork)
        input("\nTekan Enter untuk kembali ke menu...")
    elif choice == '4':
        clear_screen()
        display_ascii("Mood Booster")
        mood_booster()
    elif choice == '5':
        generate_sqlmap_command()
    elif choice == '6':
        exit_toolkit() # Mengakhiri loop dan keluar dari program
    else:
        print(colored("Pilihan tidak valid! Coba lagi.", 'red'))
        time.sleep(2)

if __name__ == "__main__":
    main_menu()
