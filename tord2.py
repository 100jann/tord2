import streamlit as st
import random

# Macedonian truths and dares
truths_mk = [
"Која е најголемата фантазија што ја имаш, а никогаш не си ја споделил/а?",
    "Кој е најнеобичниот комплимент што си го добил/а?",
    "Што е најсекси на лицето спроти тебе?",
    "Која е твојата омилена секси облека?",
    "Дали некогаш си пробал/а нешто што го сметаше за табу?",
    "Кога последен пат направи нешто храбро за партнерот?",
    "Што најмногу те возбудува кај партнерот од десната страна?",
    "Дали некогаш си сонувал/а за некој во оваа просторија?",
    "Која е најчудната идеја што си ја имал/а за спалната соба?",
    "Што е твојата омилена локација за интимни моменти?",
    "Дали некогаш си бил/а љубоморен/а на нечија врска?",
    "Која е најлудата работа што некогаш си ја направил/а со партнер?",
    "Дали некогаш си сакал/а да испробаш нешто, но те било срам да прашаш?",
    "Што најмногу цениш кај лицето од левата страна?",
    "Дали некогаш си пробал/а улога или игра во спалната соба?",
    "Кој е твојот омилен дел од телото на партнерот?",
    "Што е нешто што никогаш не би направил/а дури и да те замолат?",
    "Дали некогаш си размислувал/а да направиш нешто неочекувано со партнер?",
    "Која е најголемата тајна што си ја чувал/а од партнер?",
    "Кој момент со партнерот ти остана незаборавен?",
    "Што е најинтимното нешто што си го кажал/а некогаш?",
    "Дали некогаш си се почувствувал/а виновен/а поради нешто што си направил/а?",
    "Која е најромантичната работа што си ја направил/а за некого?",
    "Што е твојот омилен спомен со лицето спроти тебе?",
    "Дали некогаш си посакал/а нешто за што никогаш не си разговарал/а?",
    "Која е најголемата авантура што си ја имал/а со партнер?",
    "Дали некогаш си се фатил/а дека мислиш на нешто неприкладно?",
    "Која е најголемата лага што си ја кажал/а некогаш?",
    "Која е најромантичната работа што партнерот некогаш ја направил за тебе?",
    "Која е најсмешната работа што ти се случила за време на интимен момент?",
    "Дали некогаш си имал/а момент каде што едвај си се воздржал/а?",
    "Што е нешто што најмногу би сакал/а да пробаш, но не си сигурен/а како да прашаш?",
    "Кој е најнезгодниот момент што си го доживеал/а во романтична ситуација?",
    "Што е првото нешто што те привлекува кај партнер?",
    "Дали некогаш си почувствувал/а силна привлечност кон некој пријател?",
    "Кој е најдобриот комплимент што некогаш си го добил/а од партнер?",
    "Дали некогаш си помислил/а дека ќе ти се допадне нешто неочекувано?",
    "Која е твојата омилена меморија со некој во оваа просторија?",
    "Дали некогаш си имал/а чувство дека некој го чита твојот ум?"
]

dares_mk = [
    "Дозволи му на лицето од твојата лева страна да избере кое парче облека ќе соблечеш.",
    "Соблечи едно парче облека и остави го на средината од кругот.",
    "Замени едно парче облека со лицето од твојата десна страна.",
    "Додека соблекуваш едно парче облека, кажи му нешто секси на лицето спроти тебе.",
    "Дозволи му на лицето десно од тебе да ти соблече парче облека користејќи само една рака.",
    "Допирајте го за препони 20 секунди лицето од десната страна.",
    "Масирај го 1 минута на рамената лицето од левата страна додека со устата му дишеш зад увото и вратот.",
    "Пробај да го напалиш второто лице од твојата лева страна.",
    "Со затворени очи, допри некого во групата и погоди кој е.",
    "Допри ја раката на лицето спроти тебе и задржи ја така до твојот следен предизвик.",
    "Со лесен допир, помини низ косата на лицето од левата страна.",
    "Допрете ги градите на лицето од десната страна за 5 секунди.",
    "Лицето од левата страна нека те прегрне 10 секунди.",
    "Лесно допри го колкот на лицето од десната страна.",
    "Направи бавен танц со лицето од десната страна.",
    "Бакни го лицето од левата страна.",
    "Направете контакт со очи со лицето од левата страна и кажете нешто секси.",
    "Лесно помини со прст по вратот на лицето од десната страна.",
    "Направи 10-секундно интимно гушкање со лицето спроти тебе.",
    "Подели секси тајна со лицето од левата страна (шепни му).",
    "Направи интимен гест кон лицето од левата страна (без допир).",
    "Замоли го лицето од десната страна за секси танц.",
    "Наслони се на рамото на лицето од левата страна 10 секунди.",
    "Кажи еден секси коментар за лицето од левата страна.",
    "Изведи секси шега со лицето од десната страна.",
    "Направете провокативна поза со лицето од левата страна.",
    "Направете 10-секундно секси гледање во очи со лицето од десната страна.",
    "Импровизирајте секси движење за 10 секунди.",
    "Танцувајте со групата додека соблекувате едно парче облека.",
    "Седнете во скутот на лицето од спротивниот пол на другиот пар и остани така до твојот следен предизвик.",
    "Бакни го соиграчот од ист пол.",
    "Дозволи му на соиграчот од спротивниот пол и пар да се напие пијалок од вашите гради.",
]

# Turkish truths and dares
truths_tr = [
"Sahip olduğun en büyük fantezi nedir, asla paylaşmadığın?",
    "Aldığın en tuhaf iltifat nedir?",
    "Karşındaki kişide en seksi olan nedir?",
    "En sevdiğin seksi kıyafet nedir?",
    "Hiç tabu olduğunu düşündüğün bir şey denedin mi?",
    "Son olarak partnerin için ne zaman cesur bir şey yaptın?",
    "Sağındaki partnerinde seni en çok ne heyecanlandırıyor?",
    "Bu odada biriyle hiç rüya gördün mü?",
    "Yatak odası için en tuhaf fikrin neydi?",
    "En sevdiğin özel anlar için hangi yer en uygun?",
    "Başka birinin ilişkisinden hiç kıskandın mı?",
    "Partnerinle yaptığın en çılgın şey neydi?",
    "Denemek istediğin ama sormaya çekindiğin bir şey oldu mu?",
    "Solundaki kişide en çok neyi takdir ediyorsun?",
    "Yatak odasında hiç rol yapmayı ya da oyun oynamayı denedin mi?",
    "Partnerinin vücudundaki en sevdiğin yer nedir?",
    "İstediğin bir şeyi yapmamayı, hatta sana rica edilse bile kabul etmeyeceğin bir şey var mı?",
    "Partnerinle hiç beklenmedik bir şey yapmayı düşündün mü?",
    "Partnerine sakladığın en büyük sır neydi?",
    "Partnerinle yaşadığın en unutulmaz an neydi?",
    "Şimdiye kadar söylediğin en samimi şey neydi?",
    "Yaptığın bir şeyden dolayı hiç suçlu hissettin mi?",
    "Birine yaptığın en romantik şey neydi?",
    "Karşındaki kişiyle en sevdiğin anı nedir?",
    "Hiç konuşmadığın ama arzu ettiğin bir şey var mı?",
    "Partnerinle yaşadığın en büyük macera neydi?",
    "Hiç uygunsuz bir şey düşündüğünü fark ettin mi?",
    "Şimdiye kadar söylediğin en büyük yalan neydi?",
    "Partnerinin senin için yaptığı en romantik şey neydi?",
    "İntim bir anı yaşarken yaşadığın en komik şey neydi?",
    "Hiç kendini zor tutamadığın bir an oldu mu?",
    "Denemek istediğin ama nasıl sorman gerektiğinden emin olmadığın bir şey var mı?",
    "Romantik bir durumda yaşadığın en garip an neydi?",
    "Partnerinle seni en çok çeken şey nedir?",
    "Hiç bir arkadaşına güçlü bir şekilde çekim hissettin mi?",
    "Partnerinden aldığın en güzel iltifat nedir?",
    "Hiç beklenmedik bir şeyi beğeneceğini düşündün mü?",
    "Bu odada birisiyle yaşadığın en güzel anın neydi?",
    "Bazen başkalarının zihinlerini okuduğunu hissettin mi?"
]

dares_tr = [
    "Solundaki kişiye, hangi kıyafeti çıkaracağını seçmesine izin ver.",
    "Bir parça kıyafet çıkar ve onu çemberin ortasına bırak.",
    "Bir parça kıyafetini sağındaki kişiyle değiştir.",
    "Bir parça kıyafet çıkarırken karşındaki kişiye seksi bir şey söyle.",
    "Sağındaki kişiye, tek elle kıyafetini çıkarmasına izin ver.",
    "Sağındaki kişiyi 20 saniye boyunca dizinden tutarak dokun.",
    "Solundaki kişiye, kulağının ve boynunun arkasına nefes alarak 1 dakika masaj yap.",
    "Solundaki ikinci kişiyi tahrik etmeye çalış.",
    "Gözlerini kapat, gruptaki birine dokun ve kim olduğunu tahmin et.",
    "Karşındaki kişinin elini tut ve onu bir sonraki meydan okumanıza kadar böyle tut.",
    "Solundaki kişinin saçını nazikçe elinle geç.",
    "Sağındaki kişinin göğsüne 5 saniye boyunca dokun.",
    "Solundaki kişi seni 10 saniye boyunca kucaklasın.",
    "Sağındaki kişinin kalçasına nazikçe dokun.",
    "Sağındaki kişiyle yavaşça dans et.",
    "Solundaki kişiyi öp.",
    "Solundaki kişiyle göz teması kur ve seksi bir şey söyle.",
    "Sağındaki kişinin boynunda parmak uçlarınla nazikçe geç.",
    "Karşındaki kişiyle 10 saniye boyunca samimi bir sarılma yap.",
    "Solundaki kişiyle seksi bir sır paylaş (fısılda).",
    "Solundaki kişiye dokunmadan samimi bir hareket yap.",
    "Sağındaki kişiye seksi bir dans yapmasını söyle.",
    "Solundaki kişinin omzuna yaslan ve 10 saniye bekle.",
    "Solundaki kişi için seksi bir yorum yap.",
    "Sağındaki kişiyle seksi bir şaka yap.",
    "Solundaki kişiyle provokatif bir poz yap.",
    "Sağındaki kişiyle 10 saniye boyunca seksi göz teması yap.",
    "10 saniye boyunca seksi bir hareket improvize et.",
    "Grup ile birlikte dans ederken bir parça kıyafet çıkar.",
    "Karşı cinsinle olan kişinin kucağında otur ve bir sonraki meydan okumana kadar böyle kal.",
    "Aynı cinsten oyuncuyu öp.",
    "Farklı cinsiyet grubundan oyuncuya, göğüslerinden bir içki içmesini söyle."
]

st.title("Вистина или Предизвик / Doğruluk mu Cesaret mi")

# Custom CSS for styling
st.markdown("""
    <style>
        .truth-dare-container {
            background-color: #f7f7f7;
            padding: 20px;
            border-radius: 8px;
            border: 2px solid #d1d1d1;
            margin-top: 20px;
            margin-bottom: 20px;
            font-size: 18px;
            font-weight: bold;
            text-align: left;
        }
        .button-container {
            margin-top: 20px;
            text-align: center;
        }
        .button-container button {
            background-color: #4CAF50;
            color: white;
            padding: 15px 32px;
            font-size: 16px;
            cursor: pointer;
            border: none;
            border-radius: 8px;
        }
        .button-container button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# Кликнување на копчето "Вистина"
if st.button("Вистина / Doğruluk"):
    # Случаен избор на вистина
    idx = random.randint(0, len(truths_mk) - 1)
    truth_mk = truths_mk[idx]
    truth_tr = truths_tr[idx]

    # Прикажување на резултатите во стилска кутија
    st.markdown(f"""
        <div class="truth-dare-container">
            <p><strong>Вистина:</strong> {truth_mk}</p>
            <p><strong>Doğruluk:</strong> {truth_tr}</p>
        </div>
    """, unsafe_allow_html=True)

# Кликнување на копчето "Предизвик"
if st.button("Предизвик / Cesaret"):
    # Случаен избор на предизвик
    idx = random.randint(0, len(dares_mk) - 1)
    dare_mk = dares_mk[idx]
    dare_tr = dares_tr[idx]

    # Прикажување на резултатите во стилска кутија
    st.markdown(f"""
        <div class="truth-dare-container">
            <p><strong>Предизвик:</strong> {dare_mk}</p>
            <p><strong>Cesaret:</strong> {dare_tr}</p>
        </div>
    """, unsafe_allow_html=True)

# Кликнување на копчето "Random"
if st.button("Random"):
    # Случаен избор на дали ќе биде вистина или предизвик
    choice = random.choice(["truth", "dare"])
    
    if choice == "truth":
        # Случаен избор на вистина
        idx = random.randint(0, len(truths_mk) - 1)
        truth_mk = truths_mk[idx]
        truth_tr = truths_tr[idx]

        # Прикажување на резултатите во стилска кутија
        st.markdown(f"""
            <div class="truth-dare-container">
                <p><strong>Вистина:</strong> {truth_mk}</p>
                <p><strong>Doğruluk:</strong> {truth_tr}</p>
            </div>
        """, unsafe_allow_html=True)
    
    elif choice == "dare":
        # Случаен избор на предизвик
        idx = random.randint(0, len(dares_mk) - 1)
        dare_mk = dares_mk[idx]
        dare_tr = dares_tr[idx]

        # Прикажување на резултатите во стилска кутија
        st.markdown(f"""
            <div class="truth-dare-container">
                <p><strong>Предизвик:</strong> {dare_mk}</p>
                <p><strong>Cesaret:</strong> {dare_tr}</p>
            </div>
        """, unsafe_allow_html=True)
