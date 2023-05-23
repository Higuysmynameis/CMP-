from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
import psycopg2
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivymd.uix.menu import MDDropdownMenu


class FirstScreen(Screen):
    pass


class MenuScreen(Screen):
    email = ObjectProperty(None)
    trash = ObjectProperty(None)
    user = ObjectProperty(None)
    start = ObjectProperty(None)
    database = psycopg2.connect(host="localhost", dbname="postgres", user="postgres",
                                password="Ransana@2008", port=5432)
    print("Database connection established.")
    cursor = database.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS person(
        id INT PRIMARY KEY,
        name VARCHAR(255),
        trash INT,
        place VARCHAR(255)
        );""")
    print("Table created successfully.")

    database.commit()
    def handle_search(self):

        print("Search button clicked")

    def handle_dots(self):
        print("Dots button clicked")
    # def logger(self):
    #     self.start.text = f'Welcome {self.user.text}'
    def test1(self):
        print("Test1 is pressed")

    def test2(self):
        print("Test2 is pressed")

    def clear(self):
        self.start.text = "Beatification And Gamification"
        self.user.text = ""
        self.trash.text = ""
        self.place.text = ""

    def send_data(self, place, user, trash):
        self.self.cursor.execute(
            f"INSERT INTO person (name, trash, place) VALUES (%s, %s, %s)",
            ({place.text}, {user.text}, {int(trash.text)})
        )
        self.cursor.execute("DELETE FROM person WHERE id=1;")
        self.database.commit()

    def on_leave(self):
        self.cursor.close()
        self.database.close()


class GalleryScreen(Screen):
    def handle_menu(self):
        print("Menu button clicked")

    def handle_search(self):

        print("Search button clicked")

    def handle_dots(self):
        print("Dots button clicked")


class ProfileScreen(Screen):
    def handle_search(self):
        print("Search button clicked")

    def handle_dots(self):
        print("Dots button clicked")


class SecondScreen(Screen):
    pass


# sm = ScreenManager()
# sm.add_widget(MenuScreen(name='menu'))
# sm.add_widget(ProfileScreen(name='profile'))


sm = ScreenManager()
sm.add_widget(FirstScreen(name='info'))
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(GalleryScreen(name='gallery'))


class MainApp(MDApp):
    def build(self):
        self.title = "Beatification and Gamification"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(
            '''
ScreenManager:
    MenuScreen:
    ProfileScreen:
    GalleryScreen:

<GalleryScreen>:
    name: "gallery"
    orientation: "vertical"
    MDTopAppBar:
        title: "Gallery"
        pos_hint: {"top": 1}
        elevation: 10
        text_color: 0, 0, 0, 0  # Black text color
        md_bg_color: 0, 0, 0, 1

        right_action_items: [["arrow-left", lambda x: root.handle_search], ["arrow-right", lambda x: root.handle_dots()]]

    MDScrollView:
        size_hint: 1, None
        height: "850dp"  # Adjust the height as needed

        MDGridLayout:
            id: grid
            cols: 1
            spacing: "10dp"
            adaptive_height: True
            padding: "10dp"
            size_hint_y: None
            height: self.minimum_height
            pos_hint: {"center_y": 0.5, "center_x": 0.5}


            MDSmartTile:
                radius: 24
                box_radius: [0, 0, 24, 24]
                lines: 2
                source: "C:/risinu2.0/CMP/alt-5a5d0e2b603d9-4747-e83eca4462779e6a9e93b39c0720961d@1x.jpg"
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                size_hint: None, None
                size: "500dp", "500dp"

            MDIconButton:
                icon: "heart-outline"
                theme_icon_color: "Custom"
                icon_color: 1, 0, 0, 1
                pos_hint: {"center_y": 0.5}
                on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

            TwoLineListItem:
                text: "[color=#ffffff][b]Trash[/b][/color]"
                secondary_text: "[color=#808080][b]Richard Lee[/b][/color]"
                pos_hint: {"center_y": .5}
                _no_ripple_effect: True

            MDSmartTile:
                radius: 24
                box_radius: [0, 0, 24, 24]
                lines: 2
                source: "C:/risinu2.0/CMP/20230518_010008538_iOS.jpg"
                pos_hint: {"center_x": 0.8, "center_y": 0.5}
                size_hint: None, None
                size: "500dp", "500dp"

            MDIconButton:
                icon: "heart-outline"
                theme_icon_color: "Custom"
                icon_color: 1, 0, 0, 1
                pos_hint: {"center_y": 0.5}
                on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

            TwoLineListItem:
                text: "[color=#ffffff][b]Bannana[/b][/color]"
                secondary_text: "[color=#808080][b]Richard Lee[/b][/color]"
                pos_hint: {"center_y":  .5}
                _no_ripple_effect: True

            MDSmartTile:
                radius: 24
                box_radius: [0, 0, 24, 24]
                lines: 2
                source: "C:/risinu2.0/CMP/20230518_011409864_iOS.jpg"
                pos_hint: {"center_x": 0.8, "center_y": 0.5}
                size_hint: None, None
                size: "500dp", "500dp"

            MDIconButton:
                icon: "heart-outline"
                theme_icon_color: "Custom"
                icon_color: 1, 0, 0, 1
                pos_hint: {"center_y": 0.5}
                on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

            TwoLineListItem:
                text: "[color=#ffffff][b]Wrapper[/b][/color]"
                secondary_text: "[color=#808080][b]Richard Lee[/b][/color]"
                pos_hint: {"center_y":  .5}
                _no_ripple_effect: True

            MDSmartTile:
                radius: 24
                box_radius: [0, 0, 24, 24]
                lines: 2
                source: "C:/risinu2.0/CMP/20230518_010031501_iOS.jpg"
                pos_hint: {"center_x": 0.8, "center_y": 0.5}
                size_hint: None, None
                size: "500dp", "500dp"

            MDIconButton:
                icon: "heart-outline"
                theme_icon_color: "Custom"
                icon_color: 1, 0, 0, 1
                pos_hint: {"center_y": 0.5}
                on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

            TwoLineListItem:
                text: "[color=#ffffff][b]Drink[/b][/color]"
                secondary_text: "[color=#808080][b]Richard Lee[/b][/color]"
                pos_hint: {"center_y":  .5}
                _no_ripple_effect: True


<ProfileScreen>:
    name: "profile"
    MDTopAppBar:
        title: "Info"
        pos_hint: {"top": 1}
        elevation: 10
        text_color: 0, 0, 0, 0  # Black text color
        md_bg_color: 0, 0, 0, 1

        right_action_items: [["arrow-left", lambda x: root.handle_search], ["arrow-right", lambda x: root.handle_dots()]]
    MDCard:
        size_hint: None, None
        size: 800, 800
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 10
        padding: 25
        spacing: 25
        color: (0.4, 0.6, 1.0, 1.0)
        orientation: 'vertical'

        MDLabel:
            id: poll
            text: "Be part of the solution not the pollution"
            font_size: 40
            color: (0.4, 0.6, 1.0, 1.0)

            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 15

        MDLabel:
            id: pollin
            text: "Littering is a harmful practice that negatively impacts the environment, human health, and wildlife. Our project aims to combat littering and promote a cleaner, healthier QASMT. By raising awareness through educational campaigns, implementing proper waste disposal infrastructure, and organizing community clean-up events, we strive to instill a sense of responsibility and encourage sustainable practices. Together, we can create a cleaner environment, protect our natural resources, and foster a culture of cleanliness and respect for our surroundings. Join us in our mission to reduce littering and make a lasting difference."
            font_size: 24
            color: (0.4, 0.7, 1.0, 1.0)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 15
        MDSmartTile:
            radius: 24
            box_radius: [0, 0, 24, 24]
            box_color: 1, 1, 1, .2
            source: "C:/risinu2.0/CMP/alt-5a5d0e2b603d9-4747-e83eca4462779e6a9e93b39c0720961d@1x.jpg"
            pos_hint: {"center_x": .5, "center_y": .5}
            size_hint: None, None
            size: "200dp", "200dp"

        MDRoundFlatButton:
            text: "Back to submission"

            font_size: 18
            pos_hint: {"center_x": 0.5}
            on_press:
                root.manager.current = 'menu'
            on_release:
                root.manager.transition.direction = "left"

        MDRoundFlatButton:
            text: "Gallery"

            font_size: 18
            pos_hint: {"center_x": 0.5}
            on_press:
                root.manager.current = 'gallery'
            on_release:
                root.manager.transition.direction = "left"


<FirstScreen>:
    name: "info"
    MDTopAppBar:
        title: "Gallery"
        pos_hint: {"top": 1}
        elevation: 10
        text_color: 0, 0, 0, 0  # Black text color
        md_bg_color: 0, 0, 0, 1

        right_action_items: [["arrow-left", lambda x: root.handle_search], ["arrow-right", lambda x: root.handle_dots()]]
    MDCard:
        size_hint: None, None
        size: 500, 500
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'

    MDRoundFlatButton:
        text: "back to submission"

        font_size: 18
        pos_hint: {"center_x": 0.5}
        on_press:
            root.manager.current = 'menu'
        on_release:
            root.manager.transition.direction = "left"


<MenuScreen>:
    name: "menu"
    start: start
    user: user
    trash: trash
    MDTopAppBar:
        title: "Submission"
        pos_hint: {"top": 1}
        elevation: 10
        text_color: 0, 0, 0, 0  # Black text color
        md_bg_color: 0, 0, 0, 1

        right_action_items: [["arrow-left", lambda x: root.handle_search], ["arrow-right", lambda x: root.handle_dots()]]
        place: place
    MDCard:
        size_hint: None, None
        size: 800, 700
        color: (0, 1, 0, 1)
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 10
        padding: 25
        spacing: 25

        orientation: 'vertical'

        MDLabel:
            id: start
            text: "Litter Learners"
            font_size: 50
            color: (0.4, 0.6, 1.0, 1.0)

            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 15

        MDTextField:
            id: user
            hint_text: "Name"
            color: (0.4, 0.6, 1.0, 1.0)
            icon_right: "account"
            size_hint_x: None
            width: 200
            font_size: 28
            pos_hint: {"center_x": 0.5}

        MDTextField:
            id: trash
            hint_text: "Trash collected"
            color: (0.4, 0.6, 1.0, 1.0)
            icon_right: "trash-can"
            size_hint_x: None
            width: 200
            font_size: 28
            pos_hint: {"center_x": 0.5}

        MDTextField:
            id: place
            hint_text: "Block found"
            color: (0.4, 0.6, 1.0, 1.0)
            icon_right: "office-building"
            size_hint_x: None
            width: 200
            font_size: 28
            pos_hint: {"center_x": 0.5}

        MDDropDownItem:
            id: drop
            pos_hint: {"center_x": 0.5}
            text: "Place"
            on_release: self.set_item["1, 2"]

        MDRoundFlatButton:
            text: "Submit"

            font_size: 18
            pos_hint: {"center_x": 0.5}
            on_press:
                root.manager.current = 'profile'
            on_release:
                root.send_data(user, place, trash)
                root.manager.transition.direction = "left"

        MDRoundFlatButton:
            text: "Click for more info"

            font_size: 18
            pos_hint: {"center_x": 0.5}
            on_press:
                root.manager.current = 'profile'
            on_release:
                root.manager.transition.direction = "left"


        MDRoundFlatButton:
            text: "Clear"

            font_size: 18
            pos_hint: {"center_x": 0.5}
            on_press: root.clear()
            
            '''
        )
    #
    # def logger(self):
    #     self.root.ids.start.text = f'Welcome {self.root.ids.user.text}'
    #
    # def clear(self):
    #     self.root.ids.start.text = "Beatification And Gamification"
    #     self.root.ids.user.text = ""
    #     self.root.ids.trash.text = ""
    #     self.root.ids.email.text = ""
    #
    # def send_data(self, email, user, trash):
    #     self.cursor.execute(f"insert into logindata values('{email.text}', '{user.text}', '{trash.text}')")
    #     self.database.commit()


MainApp().run()
