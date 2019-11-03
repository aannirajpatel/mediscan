package tech.aanpatel.mediscan;

import android.content.DialogInterface;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.drawable.BitmapDrawable;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.InputType;
import android.util.Base64;
import android.util.Log;
import android.view.View;
import android.view.ViewTreeObserver;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.google.gson.Gson;

import java.io.BufferedReader;
import java.io.ByteArrayOutputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class SelectFields extends AppCompatActivity {
    private String fieldName = "";
    private List<String> fieldList = new ArrayList<String>();
    private List<int[]> coordList = new ArrayList<int[]>();
    private int[] ivCoords = new int[2];
    private int[] rectCoords;
    ImageView iv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_select_fields);
        Intent intent = getIntent();
        Bundle bundle = intent.getExtras();
        String currentPhotoPath = bundle.getString("BitmapImagePath");
        BitmapFactory.Options bmOptions = new BitmapFactory.Options();
        Bitmap bitmap = BitmapFactory.decodeFile(currentPhotoPath, bmOptions);
        iv = findViewById(R.id.formImage);
        bitmap = Bitmap.createScaledBitmap(bitmap, iv.getWidth(), iv.getHeight(), true);
        iv.setImageBitmap(bitmap);
        /*getViewTreeObserver().addOnGlobalLayoutListener(new ViewTreeObserver.OnGlobalLayoutListener() {
            public void onGlobalLayout() {
                getViewTreeObserver().removeGlobalOnLayoutListener(this);
                iv.getLocationOnScreen(ivCoords);
                int x = ivCoords[0];
                int y = ivCoords[1];
            }
        });*/

    }

    private int fieldImgXY[] = new int[2];

    @Override
    public void onWindowFocusChanged(boolean hasFocus) {
        super.onWindowFocusChanged(hasFocus);

        // Use onWindowFocusChanged to get the placement of
        // the image because we have to wait until the image
        // has actually been placed on the screen  before we
        // get the coordinates. That makes it impossible to
        // do in onCreate, that would just give us (0, 0).
        iv.getLocationOnScreen(ivCoords);
        Log.i("INFO", "IVC: " + ivCoords[0] + ivCoords[1]);
    }

    public void addField(View view) {
        final DragRectView addFieldRectView = (DragRectView) findViewById(R.id.add_field_rect_view);
        if (addFieldRectView.getIsLegitRectangle()) {
            rectCoords = new int[4];
            addFieldRectView.getNormalizedCoords(rectCoords);
            addFieldRectView.resetRect();
            AlertDialog.Builder builder = new AlertDialog.Builder(SelectFields.this);
            builder.setTitle("Enter field name");

// Set up the input
            final EditText input = new EditText(SelectFields.this);
// Specify the type of input expected; this, for example, sets the input as a password, and will mask the text
            input.setInputType(InputType.TYPE_CLASS_TEXT | InputType.TYPE_TEXT_VARIATION_NORMAL);
            builder.setView(input);

// Set up the buttons
            builder.setPositiveButton("OK", new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int which) {
                    fieldName = input.getText().toString();
                    //Add fieldName to a list
                    fieldList.add(fieldName);
                    Log.i("INFO", "Field " + fieldName + " added");
                    TextView tv = findViewById(R.id.statusMessage);
                    tv.setText("Status: Field " + fieldName + " added");
                    ImageView iv = findViewById(R.id.formImage);
                    rectCoords[0] -= ivCoords[0];
                    rectCoords[1] -= ivCoords[1];
                    rectCoords[2] -= ivCoords[0];
                    rectCoords[3] -= ivCoords[1];
                    //Find coordinates of rect wrt image topleft and add them to a list
                    coordList.add(rectCoords);
                }
            });
            builder.setNegativeButton("Cancel", new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int which) {
                    dialog.cancel();
                }
            });

            builder.show();
        }
        //Ask for field name if the rectangle is selected. Otherwise, say that you need to select a rectangle.
        else {
            TextView tv = findViewById(R.id.statusMessage);
            tv.setText("Status: Please highlight a field!");
        }
        // If nothing was selected, toast appropriate msg and return

    }

    public void sendData(View view) {
        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
        BitmapDrawable drawable = (BitmapDrawable) iv.getDrawable();
        Bitmap bitmap = drawable.getBitmap();
        bitmap.compress(Bitmap.CompressFormat.PNG, 100, byteArrayOutputStream);
        byte[] byteArray = byteArrayOutputStream.toByteArray();
        String encoded = Base64.encodeToString(byteArray, Base64.DEFAULT);
        HashMap<String, Object> dataToSend = new HashMap<>();
        dataToSend.put("fields", fieldList);
        dataToSend.put("coords", coordList);
        dataToSend.put("img", encoded);
        Log.i("INFO", "JSON::" + new Gson().toJson(dataToSend));
        String jsonToSend = new Gson().toJson(dataToSend);

        try {
            URL url = new URL("https://mediscan-257820.appspot.com");
            HttpURLConnection con = (HttpURLConnection) url.openConnection();
            con.setRequestMethod("POST");
            con.setRequestProperty("Content-Type", "application/json; utf-8");
            con.setRequestProperty("Accept", "application/json");
            con.setDoOutput(true);
            try (OutputStream os = con.getOutputStream()) {
                byte[] input = jsonToSend.getBytes("utf-8");
                os.write(input, 0, input.length);
            }
            try (BufferedReader br = new BufferedReader(new InputStreamReader(con.getInputStream(), "utf-8"))) {
                StringBuilder response = new StringBuilder();
                String responseLine = null;
                while ((responseLine = br.readLine()) != null) {
                    response.append(responseLine.trim());
                }
                Log.i("INFO","RESPONSE:"+response.toString());
            }
        } catch (Exception e) {
            Log.i("INFO", e.getMessage());
        }
    }
}
