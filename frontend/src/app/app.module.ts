import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


import { AppComponent } from './app.component';
import { WeighingListComponent } from './weighing-list/weighing-list.component';
import { WeighingEditComponent } from './weighing-edit/weighing-edit.component';


@NgModule({
  declarations: [
    AppComponent,
    WeighingListComponent,
    WeighingEditComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
  title = 'Stats';
}
