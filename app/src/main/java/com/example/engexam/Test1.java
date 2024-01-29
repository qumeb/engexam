package com.example.engexam;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.LinearLayout;

import java.lang.reflect.Array;

public class Test1 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.universal);

    }
    public void onClickBack(View view) {
        try {
            Intent intent = new Intent(Test1.this, MainActivity.class);
            startActivity(intent);
            finish();
        }catch (Exception e){
            //
        }
    }

    public void onClickNext(View view) {


        try {
            Intent intent1 = new Intent(Test1.this, Test2.class);
            startActivity(intent1);
            finish();
        }catch (Exception e){
            //
        }
    }
}