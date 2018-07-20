import java.util.ArrayList;
import java.util.LinkedList;

class Album
{
    private String name,artist;
    private ArrayList<Song> songs;

    public Album(String name, String artist) {
        this.name = name;
        this.artist = artist;
        this.songs = new ArrayList<Song>();
    }
    public boolean addSong(String title,double duration){
        if(findSong(title)==null){
            this.songs.add(new Song(title, duration));
            return true;
        }return false;

    }
    public Song findSong(String title){
        for(Song checkedSong:this.songs){
            if(checkedSong.getTitle().equals(title)){
                return checkedSong;
            }
        }return null;
    }
    public boolean addToPlaylist(int trackNumber, LinkedList<Song> playlist){
        int index=trackNumber-1;
        if((index>=0)&&(index<=this.songs.size())){
            playlist.add(this.songs.get(index));
            return true;
        }
        System.out.println("This album does not have a track ="+trackNumber);
        return false;
    }

    public boolean addToPlaylist(String title,LinkedList<Song> playlist){
        Song checkedSong=findSong(title);
        if(checkedSong!=null){
            playlist.add(checkedSong);
            return true;
        }
        System.out.println("The song "+title+" is not in album");
        return false;
    }

}