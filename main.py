from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, RoundedRectangle, Rectangle
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.animation import Animation
from kivy.properties import ListProperty
import os
import random

BOJA_POZADINE = (1.0, 0.89, 0.94, 1)
BOJA_KARTICE = (1.0, 0.98, 0.99, 1)
BOJA_TEKSTA = (0.44, 0.0, 0.22, 1)
BOJA_SVETLI_TEKST = (0.63, 0.30, 0.44, 1)
BOJA_DUGMETA = (1.0, 0.56, 0.73, 1)
BOJA_DUGMETA_PRITISAK = (1.0, 0.44, 0.66, 1)
BOJA_BORDURE = (1.0, 0.67, 0.82, 1)

SLAJDOVI = [
    ("divna.jpg", "JE DIVNA! ❤️"),
    ("pametna.jpg", "JE PAMETNA! 🧠"),
    ("dioptrija.jpg", "👓 JOJ JE JEDINI MINUS – MINUS DIOPTRIJA"),
    ("dobra.jpg", "JE DOBRA! 😇"),
    ("japanski.jpg", "PRIČA JAPANSKI"),
    ("knjige.jpg", "NABAVLJA KNJIGE\nnekad i preko veze"),
    ("logo1.jpg", "JOJ DRUGI LOGOPEDI NE MOGU NIŠTA!"),
    ("klompe.jpg", "🤍 JOJ KLOMPE NA HALJINU STOJE PREKUL! 🤍"),
    ("sushi.jpg", "VOLI SUŠI..."),
    ("sushi2.jpg", "...I BEZ UŠI."),
    ("zmaj.jpg", "VOLI ČIKA JOVU-ZMAJA"),
    ("kafa.jpg", "KUVA DOVOLJNO PREPRODUŽENU KAFU IZ APARATA ☕"),
    ("asvaganda.jpg", "AŠVAGANDA MOŽE DA MIRIŠE NA NJU"),
    ("kulturna.jpg", "JE KULTURNA"),
    ("humor1.jpg", "IMA SMISLA ZA HUMOR..."),
    ("humor2.jpg", "...I CRNI HUMOR."),
    ("jung1.jpg", "ČITA JUNGA..."),
    ("jung2.jpg", "...RAZUME JUNGA!"),
    ("folklor.jpg", "NE TREBA JOJ GPT DA RAZVALI KOREOGRAFIJU"),
    ("aiesec.jpg", "AIESEC NIJE VREDAN NI JEDNE JEDINE -SEC OTKAKO JE OTIŠLA"),
    ("deca.jpg", "USREĆI VIŠE DECE NEGO ŠTO ĆE IKAD SAZNATI ❤️"),
    ("pollo.jpg", "JE OTKRILA POLLO TZATZIKI IZ STEFANA"),
    ("tikvice.jpg", "Nikog i ništa ne mrzi...\nskoro"),
    ("biblioteka.jpg", "UNOSI MIR U BIBLIOTEKU 📚"),
    ("mir.jpg", "...I INAČE 🕊️"),
    ("nobel.jpg", "JE ČEKA NOBELOVA NAGRADA!"),
    ("cigare.jpg", "NE PUŠTA DUVANSKU INDUSTRIJU DA PROPADNE 💨"),
    ("pivo.jpg", "🍺 A BOGA MI ČUVA I SEKTOR PROIZVODNJE ALKOHOLA 🍺"),
    ("racionalna.jpg", "JE RACIONALNA ⚖️"),
    ("odmerena.jpg", "JE ODMERENA"),
    ("blaga.jpg", "JE BLAGA... 🤍"),
    ("blago.jpg", "...I BLAGO! 💰"),
    ("slusa.jpg", "ZNA DA SASLUŠA"),
    ("cinjenica.jpg", "JE UVEK VOĐENA ČINJENICAMA"),
    ("pazljiva.jpg", "JE PAŽLJIVA"),
    ("empaticna.jpg", "JE EMPATIČNA 🫂"),
    ("pronicljiva.jpg", "JE PRONICLJIVA 🔍"),
    ("ostroumna.jpg", "JE OŠTROUMNA 🧠"),
    ("pouzdana.jpg", "JE POUZDANA"),
    ("perceptivna.jpg", "JE PERCEPTIVNA 👁️"),
    ("oko.jpg", "ZATVARA LEVO OKO DOK ANALIZIRA 😉"),
    ("taxi.jpg", "TAKSIRA BESPLATNO!"),
    ("miro.jpg", "MOŽE DA RAZUME SLIKARSTVO HUANA MIROA 🎨"),
    ("porodica.jpg", "BRINE O SVOJOJ PORODICI..."),
    ("dora.jpg", "...I O DORI..."),
    ("dora2.jpg", "...KOJA SE UOPŠTE NE ZOVE DORA???\nWTF"),
    ("kolege.jpg", "BRINE O SVIM PRIJATELJIMA I KOLEGAMA 🤍"),
    ("inspirativna.jpg", "JE INSPIRATIVNA"),
    ("ratio.jpg", "IMA NAJBOLJI PAMETNO:GLUPO-IZREČENO RATIO 📈"),
    ("ne1.jpg", "NE ZNA DA KAŽE 'NE'"),
    ("ne2.jpg", "SE UČI DA KAŽE 'NE'"),
    ("uci.jpg", "SVE LAKO (NA)UČI! 🧠"),
    ("ne3.jpg", "...SEM DA KAŽE 'NE' 😂"),
    ("odgovorna.jpg", "JE ODGOVORNA 📋"),
    ("asertivna.jpg", "JE ASERTIVNA"),
    ("srdacna.jpg", "JE SRDAČNA 🤍"),
    ("katakana.jpg", "NJENU KATAKANU PREPOZNA GOOGLE TRANSLATE\nI UKOLIKO JE SMEĆE KAMERA"),
    ("aristo.jpg", "JE ARISTOKRATSKI KULTURNA..."),
    ("psuje.jpg", "...ČAK I KAD PSUJE 🤬"),
    ("hrabra.jpg", "JE HRABRA 💪"),
    ("jer.jpg", "...I NE TREBA DA BUDE TUŽNA JER..."),
    ("kraj.jpg", "NIJE MAMA P**** RODILA!!! ❤️"),
]


class RoundedPanel(BoxLayout):
    bg_color = ListProperty(BOJA_KARTICE)

    def __init__(self, radius=34, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius
        with self.canvas.before:
            Color(0.75, 0.0, 0.35, 0.20)
            self.shadow = RoundedRectangle(pos=(self.x + dp(8), self.y - dp(8)), size=self.size, radius=[dp(self.radius)])
            Color(*BOJA_KARTICE)
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[dp(self.radius)])
            Color(*BOJA_BORDURE)
            self.border = RoundedRectangle(pos=self.pos, size=self.size, radius=[dp(self.radius)])
        self.bind(pos=self._update, size=self._update)

    def _update(self, *args):
        self.shadow.pos = (self.x + dp(8), self.y - dp(8))
        self.shadow.size = self.size
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.border.pos = self.pos
        self.border.size = self.size


class OliveraApp(App):
    def build(self):
        Window.clearcolor = BOJA_POZADINE
        self.trenutni = -1
        self.folder = os.path.dirname(os.path.abspath(__file__))
        self.oki_folder = os.path.join(self.folder, "Oki")

        root = FloatLayout()
        with root.canvas.before:
            Color(*BOJA_POZADINE)
            self.bg_rect = Rectangle(pos=root.pos, size=root.size)
        root.bind(pos=self._update_bg, size=self._update_bg)

        self._dodaj_dekoracije(root)

        layout = BoxLayout(
            orientation="vertical",
            spacing=dp(8),
            padding=[dp(14), dp(12), dp(14), dp(10)],
            size_hint=(1, 1)
        )

        naslov = Label(
            text="OLIVERA NE TREBA DA BUDE TUŽNA\nZATO ŠTO...",
            font_size="25sp",
            bold=True,
            color=BOJA_TEKSTA,
            halign="center",
            valign="middle",
            size_hint_y=None,
            height=dp(78),
        )
        naslov.bind(size=lambda w, s: setattr(w, "text_size", s))

        podnaslov = Label(
            text="jedan mali, potpuno objektivan dokazni postupak",
            font_size="13sp",
            italic=True,
            color=BOJA_SVETLI_TEKST,
            halign="center",
            valign="middle",
            size_hint_y=None,
            height=dp(30),
        )
        podnaslov.bind(size=lambda w, s: setattr(w, "text_size", s))

        card_anchor = AnchorLayout(anchor_x="center", anchor_y="center", size_hint_y=1)

        self.card = RoundedPanel(
            orientation="vertical",
            spacing=dp(10),
            padding=[dp(16), dp(16), dp(16), dp(16)],
            size_hint=(0.97, 0.98),
            radius=34,
        )

        self.image_frame = BoxLayout(padding=dp(7), size_hint_y=0.70)
        with self.image_frame.canvas.before:
            Color(1, 1, 1, 1)
            self.image_bg = Rectangle(pos=self.image_frame.pos, size=self.image_frame.size)
            Color(*BOJA_BORDURE)
            self.image_border = Rectangle(pos=self.image_frame.pos, size=self.image_frame.size)
        self.image_frame.bind(pos=self._update_image_frame, size=self._update_image_frame)

        self.slika = Image(
            source=self._slika("Tuga.jpg"),
            allow_stretch=True,
            keep_ratio=True,
            opacity=1,
        )
        self.image_frame.add_widget(self.slika)

        self.tekst = Label(
            text="Klikni na dugme ❤️",
            font_size="23sp",
            bold=True,
            color=BOJA_TEKSTA,
            halign="center",
            valign="middle",
            size_hint_y=0.30,
        )
        self.tekst.bind(size=self._update_label_text_size)

        self.card.add_widget(self.image_frame)
        self.card.add_widget(self.tekst)
        card_anchor.add_widget(self.card)

        self.dugme = Button(
            text="ZAŠTO NE TREBA DA BUDE TUŽNA?",
            font_size="15sp",
            bold=True,
            color=BOJA_TEKSTA,
            background_normal="",
            background_color=BOJA_DUGMETA,
            size_hint=(0.96, None),
            height=dp(58),
        )
        self.dugme.bind(on_press=self._button_down)
        self.dugme.bind(on_release=self._button_up)

        mali = Label(
            text="Dodirni dugme za dalje",
            font_size="11sp",
            italic=True,
            color=BOJA_SVETLI_TEKST,
            size_hint_y=None,
            height=dp(22),
            halign="center",
        )

        layout.add_widget(naslov)
        layout.add_widget(podnaslov)
        layout.add_widget(card_anchor)
        layout.add_widget(self.dugme)
        layout.add_widget(mali)
        root.add_widget(layout)

        return root

    def _update_bg(self, root, *args):
        self.bg_rect.pos = root.pos
        self.bg_rect.size = root.size

    def _update_image_frame(self, *_):
        self.image_bg.pos = self.image_frame.pos
        self.image_bg.size = self.image_frame.size
        self.image_border.pos = self.image_frame.pos
        self.image_border.size = self.image_frame.size

    def _update_label_text_size(self, lbl, size):
        lbl.text_size = (max(size[0] - dp(8), 50), size[1])

    def _slika(self, ime):
        putanja = os.path.join(self.oki_folder, ime)
        return putanja if os.path.exists(putanja) else ""

    def _dodaj_dekoracije(self, root):
        simboli = ["♡", "✦", "❀", "✧", "♡"]
        boje = [
            (1.0, 0.76, 0.86, 0.48),
            (1.0, 0.82, 0.90, 0.48),
            (0.96, 0.65, 0.79, 0.48),
        ]
        for _ in range(30):
            root.add_widget(Label(
                text=random.choice(simboli),
                font_size=f"{random.randint(14, 28)}sp",
                color=random.choice(boje),
                size_hint=(None, None),
                size=(dp(40), dp(40)),
                pos_hint={"x": random.random(), "y": random.random()},
            ))

    def _podesi_tekst_i_sliku(self, tekst):
        broj_linija = tekst.count("\n") + 1
        duzina = len(tekst)

        if broj_linija >= 3 or duzina > 78:
            self.tekst.font_size = "16sp"
            self.image_frame.size_hint_y = 0.56
            self.tekst.size_hint_y = 0.44
        elif duzina > 56 or broj_linija == 2:
            self.tekst.font_size = "19sp"
            self.image_frame.size_hint_y = 0.62
            self.tekst.size_hint_y = 0.38
        else:
            self.tekst.font_size = "23sp"
            self.image_frame.size_hint_y = 0.70
            self.tekst.size_hint_y = 0.30

    def _button_down(self, *_):
        self.dugme.background_color = BOJA_DUGMETA_PRITISAK

    def _button_up(self, *_):
        self.dugme.background_color = BOJA_DUGMETA
        self.sledeci()

    def sledeci(self):
        self.trenutni += 1
        if self.trenutni >= len(SLAJDOVI):
            self.trenutni = 0

        ime, tekst = SLAJDOVI[self.trenutni]
        nova_slika = self._slika(ime)

        self._podesi_tekst_i_sliku(tekst)

        anim_out = Animation(opacity=0, duration=0.12)
        anim_in = Animation(opacity=1, duration=0.18)

        def promeni(*_):
            self.slika.source = nova_slika
            self.slika.reload()
            self.tekst.text = tekst
            anim_in.start(self.slika)

        anim_out.bind(on_complete=promeni)
        anim_out.start(self.slika)

        if self.trenutni == len(SLAJDOVI) - 1:
            self.dugme.text = "❤️ JOŠ JEDNOM OD POČETKA ❤️"
        else:
            self.dugme.text = "💗 I ZAŠTO JOŠ? 💗"


if __name__ == "__main__":
    OliveraApp().run()
