init offset = 999
screen main_menu():
    tag menu
    add gui.main_menu_background
    use navigation
    if gui.show_name:
        vbox:
            style "main_menu_vbox"
            text "[config.name!t]":
                style "main_menu_title"
            text "[config.version]":
                style "main_menu_version"
    imagebutton auto "defm64/defm64_%s.png" xpos 10 ypos 974 action OpenURL("https://allmylinks.com/defm64")
screen about():
    tag menu
    use game_menu(_("About"), scroll="viewport"):
        style_prefix "about"
        vbox:
            label "[config.name!t]"
            text _("Version [config.version!t]\n")
            if gui.about:
                text "[gui.about!t]\n"
            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")
            text _("\nPortuguese translation by {a=https://allmylinks.com/defm64}defm64{/a}.\nLicensed under {a=https://creativecommons.org/licenses/by-nc-sa/4.0/}CC BY-NC-SA 4.0{/a}.\n")
            text _("If you found this, I hope you had a great day and this game brought you smiles and laughs. That was the point of making this!")
screen preferences():
    tag menu
    use game_menu(_("Preferences"), scroll="viewport"):
        vbox:
            hbox:
                box_wrap True
                vbox:
                    style_prefix "radio"
                    label _("Language")
                    textbutton "English" action Language(None)
                    textbutton "Português" action Language("portuguese")
                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")
                    vbox:
                        style_prefix "radio"
                        label _("Rollback Side")
                        textbutton _("Disable") action Preference("rollback side", "disable")
                        textbutton _("Left") action Preference("rollback side", "left")
                        textbutton _("Right") action Preference("rollback side", "right")
                    vbox:
                        style_prefix "check"
                        label _("Skip")
                        textbutton _("Unseen Text") action Preference("skip", "toggle")
                        textbutton _("After Choices") action Preference("after choices", "toggle")
                        textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))
        vbox:
            hbox:
                box_wrap True
                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "check"
                        label _("{size=+35}       Text{/size}")
                        textbutton _("Cyan") action gui.SetPreference("color", "#00FFFF")
                        textbutton _("Yellow") action gui.SetPreference("color", "#FFFF00")
                        textbutton _("Red") action gui.SetPreference("color", "#FF0000")
                    vbox:
                        style_prefix "check"
                        label _("{size=+35}Color{/size}")
                        textbutton _("Green") action gui.SetPreference("color", "#00FF66")
                        textbutton _("White") action gui.SetPreference("color", "#FFFFFF")
                        textbutton _("Violet") action gui.SetPreference("color", "#8000FF")
                    vbox:
                        style_prefix "check"
                        label _("{size=+35}Styling{/size}")
                        textbutton _("Bold On") action gui.SetPreference("bold", True )
                        textbutton _("Bold Off") action gui.SetPreference("bold", False )
                        textbutton _("Outlines On") action gui.SetPreference("outlines", [ (5, "#000000", 0, 0) ] )
                        textbutton _("Outlines Off") action gui.SetPreference("outlines", [ (0, "#000000", 1, 1) ] )
                    vbox:
                        spacing 5
                        style_prefix "radio"
                        label _("Font Size") xalign 0.5
                        if renpy.variant("pc"):
                            textbutton _("Large") action gui.SetPreference("size", 36) alt "Change to Large Size Text" xalign 0.5
                            textbutton _("Regular") action gui.SetPreference("size", 33) alt "Change to Regular Size Text" xalign 0.5
                            textbutton _("Small") action gui.SetPreference("size", 30) alt "Change to Small Size Text" xalign 0.5
            null height (4 * gui.pref_spacing)
            hbox:
                style_prefix "slider"
                box_wrap True
                vbox:
                    label _("Text Speed")
                    bar value Preference("text speed")
                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")
                vbox:
                    if config.has_music:
                        label _("Music Volume")
                        hbox:
                            bar value Preference("music volume")
                    if config.has_sound:
                        label _("Sound Volume")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)
                    if config.has_voice:
                        label _("Voice Volume")
                        hbox:
                            bar value Preference("voice volume")
                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)
                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing
                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
image language_menu_background = "gui/main_menu2.png"
default persistent.language_selected = False
label splashscreen:
    if not persistent.language_selected:
        scene language_menu_background with fade:
            blur 15.0
        menu:
            "English":
                $ renpy.change_language(None)
                $ persistent.language_selected = True
            "Português":
                $ renpy.change_language("portuguese")
                $ persistent.language_selected = True
