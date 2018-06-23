import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WeighingEditComponent } from './weighing-edit.component';

describe('WeighingEditComponent', () => {
  let component: WeighingEditComponent;
  let fixture: ComponentFixture<WeighingEditComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WeighingEditComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WeighingEditComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
