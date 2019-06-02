import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by slade on 2019/5/31.
 */



public class tmp {
    public static void main(String[] args) {
        //array
        Integer[] arr = {1,2,3};
        // array -> list
        List list = Arrays.asList(arr);
        // array->list->arraylist
        ArrayList arrayList = new ArrayList(list);
        System.out.println(arr);
        System.out.println(list);
        System.out.println(arrayList);

        //list ->array
        Integer[] toarray = new Integer[3];
        list.toArray(toarray);
        System.out.println(toarray);

        //arraylist -> Array
        Integer[] altoarray = new Integer[3];
        arrayList.toArray(altoarray);
        System.out.println(altoarray);

        //arraylist - >Array - >list
        Integer[] arrl = new Integer[3];
        arrayList.toArray(arrl);
        List altoarraytolist = Arrays.asList(arrl);
        System.out.println(altoarraytolist);
    }
}



