import os
import Classes.LastFmApi as last_fm

def setup_out_dir(dir: str) -> None:
    if not os.path.exists(dir):
        os.mkdir(dir)

def save_csv(tracks:list, out_file:str) -> None:
    print(f'Saving {len(tracks)} tracks to {out_file}')

    with open(out_file, 'w') as writer:
        writer.writelines(f'{last_fm.csv_headers()}\n')

        for track in tracks:
            try:
                if not '@attr' in track:
                    writer.writelines(f'{last_fm.track_to_csv(track)}\n')
                else:
                    print(f"track {last_fm.get_track_name(track)} is probably playing right now")
            except Exception as ex:
                print(f"Error writing track: {ex}")

if __name__ == '__main__':
    pass
