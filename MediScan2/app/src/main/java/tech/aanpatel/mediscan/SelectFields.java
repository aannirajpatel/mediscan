package tech.aanpatel.mediscan;

import android.content.DialogInterface;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.InputType;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;

public class SelectFields extends AppCompatActivity {
    private String fieldName = "";
    private List<String> fieldList = new ArrayList<String>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_select_fields);
        Intent intent = getIntent();
        Bundle bundle = intent.getExtras();
        String currentPhotoPath = bundle.getString("BitmapImagePath");
        BitmapFactory.Options bmOptions = new BitmapFactory.Options();
        Bitmap bitmap = BitmapFactory.decodeFile(currentPhotoPath,bmOptions);
        ImageView iv = findViewById(R.id.formImage);
        bitmap = Bitmap.createScaledBitmap(bitmap,iv.getWidth(),iv.getHeight(),true);
        iv.setImageBitmap(bitmap);
        Log.i("INFO", "rfc");
    }

    public void addField(View view) {
        final DragRectView addFieldRectView = (DragRectView) findViewById(R.id.add_field_rect_view);
        if(addFieldRectView.getIsLegitRectangle()){
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
                    fieldList.add(fieldName);
                    Log.i("INFO","Field "+ fieldName + " added");
                    TextView tv = findViewById(R.id.statusMessage);
                    tv.setText("Status: Field "+fieldName+" added");
                    ImageView iv = findViewById(R.id.formImage);
                    int[] ivCoords = new int[2], rectCoords = new int[4];
                    ivCoords[0] = (int)iv.getX(); ivCoords[1] = (int)iv.getY();
                    addFieldRectView.getNormalizedCoords(rectCoords);
                    rectCoords[0]-=ivCoords[0]; rectCoords[1]-=ivCoords[1];
                    rectCoords[2]-=ivCoords[0]; rectCoords[3]-=ivCoords[1];

                    //Find coordinates of rect wrt image topleft
                    //Add fieldName to a list
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
        else{
            TextView tv = findViewById(R.id.statusMessage);
            tv.setText("Status: Please highlight a field!");
        }
        // If nothing was selected, toast appropriate msg and return

    }
}
