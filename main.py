from whatsapp.whatsapp import WhatsApp

if __name__ == '__main__':
    wa = WhatsApp(contact_name="Shaked", hours_between_msg=0.01)
    wa.run()

    print("Goodbye :)")
