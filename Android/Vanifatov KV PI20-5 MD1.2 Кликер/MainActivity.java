package com.example.clicker;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {
    TextView mainText;
    Button mainBtn;
    Button prevBtn;
    Button clrBtn;
    ImageButton imgBtn;
    String s;
    private long score = 0;

    View.OnClickListener clickListener = new View.OnClickListener() {
        @Override
        protected void onCreate(View v) {
            score++;
            if ((2 <= Math.abs(score) % 10) && (Math.abs(score) % 10 <= 4) && ((12 > Math.abs(score) % 100) || (Math.abs(score) % 100 > 14))) {
                s = "Кнопка нажата: " + score + " раза";
            } else {
                s = "Кнопка нажата: " + score + " раз";
            }
            mainText.setText(s.toCharArray(), 0, s.length())
        }
    };

    View.OnClickListener lessScore = new View.OnClickListener() {
        @Override
        public void onClick(View v) {
            score --;
            if ((2 <= Math.abs(score) % 10) && (Math.abs(score) % 10 <= 4) && ((12 > Math.abs(score) % 100) || (Math.abs(score) % 100 > 14))) {
                s = "Кнопка нажата: " + score + " раза";
            } else {
                s = "Кнопка нажата: " + score + " раз";
            }
            mainText.setText(s.toCharArray(), 0, s.length())
        }
    };

    View.OnClickListener lessScore = new View.OnClickListener() {
        @Override
        public void onClick(View v) {
            score = 0;
            String s = "Кнопка нажата 0 раз";
            mainText.setText(s.toCharArray(), 0, s.length());
        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mainText = (TextView) findViewById(R.id.mainTxt);
        mainBtn = (Button) findViewById(R.id.main_btn);
        prevBtn = (Button) findViewById(R.id.prev_btn);
        clrBtn = (Button) findViewById(R.id.clr_btn);
        imgBtn = (ImageButton) findViewById(R.id.imageButton);
        mainBtn.setOnClickListener(clickListener);
        prevBtn.setOnClickListener(lessScore);
        clrBtn.setOnClickListener(clearScore);
        imgBtn.setOnClickListener(clearScore);
    };

}