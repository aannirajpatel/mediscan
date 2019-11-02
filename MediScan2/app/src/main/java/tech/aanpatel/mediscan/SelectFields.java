package tech.aanpatel.mediscan;

import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.media.Image;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;

public class SelectFields extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_select_fields);
        Intent intent = getIntent();
        Bitmap bitmap = (Bitmap) intent.getParcelableExtra("BitmapImage");
        ImageView iv = findViewById(R.id.formImage);
        iv.setImageBitmap(bitmap);
        Log.i("INFO","rfc");
    }
}
