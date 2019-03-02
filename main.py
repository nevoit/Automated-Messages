from whatsapp.whatsapp import WhatsApp

if __name__ == '__main__':
    wa = WhatsApp(phone_name="Notes", hours_between_msg=0.01)
    wa.run()

    print("Goodbye :)")
