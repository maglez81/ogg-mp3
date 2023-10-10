from pydub import AudioSegment

def convert_ogg_to_mp3(ogg_file, mp3_file):
    # Load the ogg file
    audio = AudioSegment.from_ogg(ogg_file)

    # Export the audio as mp3
    audio.export(mp3_file, format="mp3")

if __name__ == "__main__":
    # Prompt the user for the .ogg and .mp3 filenames
    ogg_file = input("Please enter the .ogg file name: ")
    mp3_file = input("Please enter the desired name for the .mp3 file: ")

    try:
        convert_ogg_to_mp3(ogg_file, mp3_file)
        print(f"{ogg_file} has been converted to {mp3_file}")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")
