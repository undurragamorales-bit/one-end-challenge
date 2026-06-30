from dotenv import load_dotenv
from src.agent import ask_agent

load_dotenv()




def main():

    print("=" * 50)
    print("Oracle ONE AI Challenge")
    print("=" * 50)
    print()

    print("🤖 Hola, soy Laby, el asistente virtual de IA Labs. Recuerda que puedes escribir salir para terminar la conversación")
    print("🤖 Laby: Antes de comenzar, ¿cómo te llamas?")
    name = input("👤 Tú: ").strip()
    print(f"\n🤖 Laby: Mucho gusto, {name}. ¿En qué puedo ayudarte?\n")
    #print("Escribe 'salir' para terminar.\n")

    while True:

        question = input("👤 Tú: ").strip()

        if question.lower() == "salir":
            print("\n🤖 Laby: ¡Hasta luego!")
            break
        
        answer = ask_agent(name, question)

        print(f"\n🤖 Laby: {answer}\n")


if __name__ == "__main__":
    main()
