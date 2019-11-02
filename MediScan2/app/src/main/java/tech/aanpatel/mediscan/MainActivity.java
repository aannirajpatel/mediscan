package tech.aanpatel.mediscan;

import android.content.Intent;
import android.graphics.Bitmap;
import android.provider.MediaStore;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

import java.io.ByteArrayOutputStream;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button btnCamera = (Button)findViewById(R.id.btn_scan);
        //ImageView imageView = (ImageView)findViewById(R.id.imageView);

        btnCamera.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view){
                Log.i("INFO","hi2");
                Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
                Log.i("INFO","hi");
                startActivityForResult(intent, 0);
            }

        });
    }
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data){
        super.onActivityResult(requestCode, resultCode, data);
        Bitmap bitmap = (Bitmap)data.getExtras().get("data");
        Intent intent = new Intent(this, SelectFields.class);
        intent.putExtra("BitmapImage", bitmap);
        startActivity(intent);

/*

        Bundle b = new Bundle();
        b.putByteArray("image",byteArray);
*/
        // your fragment code
//        fragment.setArguments(b);
/*        ImageView iv = findViewById(R.id.imageView);
        iv.setImageBitmap(bitmap);*/
        /*Intent intent = new Intent(this, SelectFields.class);
        intent.putExtra("capturedPic",b);
        Log.i("INFO","rfc");
        startActivity(intent);
*/
        //imageView.setImageBitmap(bitmap);
    }
}
