package com.example.engexam;

import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.TextView;

import com.google.android.material.bottomnavigation.BottomNavigationView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.navigation.NavController;
import androidx.navigation.Navigation;
import androidx.navigation.ui.AppBarConfiguration;
import androidx.navigation.ui.NavigationUI;

import com.example.engexam.databinding.ActivityMainBinding;
import com.example.engexam.HttpHandler;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.concurrent.ExecutionException;

import okhttp3.OkHttpClient;

public class MainActivity extends AppCompatActivity {

    private ActivityMainBinding binding;
    ListView listView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (getSupportActionBar() != null) {
            getSupportActionBar().hide();
        }
        binding = ActivityMainBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        BottomNavigationView navView = findViewById(R.id.nav_view);
        // Passing each menu ID as a set of Ids because each
        // menu should be considered as top level destinations.
        AppBarConfiguration appBarConfiguration = new AppBarConfiguration.Builder(
                R.id.navigation_home, R.id.navigation_dashboard, R.id.navigation_notifications, R.id.navigation_favorite)
                .build();
        NavController navController = Navigation.findNavController(this, R.id.nav_host_fragment_activity_main);
        NavigationUI.setupActionBarWithNavController(this, navController, appBarConfiguration);
        NavigationUI.setupWithNavController(binding.navView, navController);

        listView = findViewById(R.id.materials_list);

        fillMaterialsList(listView);
//        TextView text = findViewById(R.id.textView);
//        Button button = findViewById(R.id.button);
//
//        button.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                HttpHandler handler = new HttpHandler();
//                handler.execute("https://fakestoreapi.com", "/products/1");
//
//                try {
//                    text.setText(handler.get().getString("title"));
//                } catch (ExecutionException | InterruptedException | JSONException e) {
//                    throw new RuntimeException(e);
//                }
//            }
//        });
    }

    private void fillMaterialsList(ListView listView) { //сделать юниверсал функцией (материалы тесты любимое)
        //1. запрос к апи (вынести все запросы в отделдьный java-класс)
        //2. по идее парсинг из json в объекты java (-//-)
        //пока пример на обычном массиве

        ArrayList<String> listItems = new ArrayList<>();
        for(int i = 0; i < 100; i++){
            listItems.add(String.valueOf(i));
        }

        System.out.println("================================================");



      ArrayAdapter<String> arrayAdapter = new ArrayAdapter<>(getApplicationContext(), com.google.android.material.R.layout.support_simple_spinner_dropdown_item, listItems);
      listView.setAdapter(arrayAdapter);
    }


}