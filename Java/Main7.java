import com.sun.xml.internal.bind.v2.runtime.reflect.ListIterator;

import java.util.ArrayList;
import java.util.LinkedList;

public class Main7 {

    private static ArrayList<Album> albums=new ArrayList<Album>();

    public static void main(String[] args) {
        Album album=new Album("Channa Mereya","Arijit Singh");
        album.addSong("Channa Mereya",5.46);
        album.addSong("Enna Sona",4.37);
        album.addSong("Ae Dil hai Mushkil",3.57);
        album.addSong("Gerua",4.25);
        album.addSong("Humdard",6.39);
        album.addSong("Hawayein",4.55);
        albums.add(album);

        album=new Album("For those who rock","AC DC");
        album.addSong("Inject the world",5.22);
        album.addSong("My world",3.34);
        albums.add(album);

        LinkedList<Song> playlist=new LinkedList<Song>();
        albums.get(0).addToPlaylist("Enna Sona",playlist);
        albums.get(0).addToPlaylist("Gerua",playlist);
        albums.get(0).addToPlaylist("Channa Mereya",playlist);
        albums.get(0).addToPlaylist("Aaj Teri",playlist);   //will fail
        albums.get(0).addToPlaylist(0,playlist);
        albums.get(1).addToPlaylist(3,playlist);
        albums.get(1).addToPlaylist(2,playlist);
        albums.get(1).addToPlaylist(10,playlist);
    }

}
