package com.example.vanifatov1;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // 1. Access the TextView defined in layout XML
        // and then set its text
        TextView mainTextView = (TextView) findViewById(R.id.main_textview);
        //mainTextView.setText("Set in Java!");

    }
}