import { Component, OnInit } from '@angular/core';
import { Producto } from 'src/models/producto.model'; // Asegúrate de importar la clase Producto
import { ApiServicio } from 'src/service/api-service';
import { ConfirmationService, MessageService, ConfirmEventType } from 'primeng/api';



@Component({
  selector: 'app-producto',
  templateUrl: './producto.component.html',
  styleUrls: ['./producto.component.css'],
  providers: [ConfirmationService, MessageService]
})

export class ProductoComponent implements OnInit {
  productos: Producto[];
  nuevoProducto: Producto = new Producto();
  esNuevoProducto: boolean;

  visible: boolean = false;

  constructor(private api:ApiServicio, private confirmationService: ConfirmationService, private messageService: MessageService){}

  ngOnInit() {
    this.obtenerProductos(); 
  }

  showCreateBox() {
    this.esNuevoProducto = true;
    this.nuevoProducto = new Producto();
    this.visible = true;
  }

  showEditBox(producto: Producto) {
    this.esNuevoProducto = false;
    this.nuevoProducto = producto;
    this.visible = true;
  }

  grabarProducto() {
    if (this.esNuevoProducto) {
      this.api.post<Producto>('producto/', this.nuevoProducto).subscribe((respuesta) => {
        this.productos.push(respuesta); 
      });
    } else {
      this.api.put<Producto>(`producto/${this.nuevoProducto.id}`, this.nuevoProducto).subscribe(() => {
        const index = this.productos.findIndex((p) => p.id === this.nuevoProducto.id);
        if (index !== -1) {
          this.productos[index] = this.nuevoProducto;
        }
      });
    }
    this.visible = false;
  }

  obtenerProductos() {
    this.api.get<Producto[]>('producto').subscribe((respuesta) => {
      this.productos = respuesta; 
    });
  }
  
  eliminarProducto(productoId: number) {

    this.api.delete<void>(`producto/${productoId}`).subscribe(() => {
      this.productos = this.productos.filter((p) => p.id !== productoId); 
    });
  }

  crearProducto(nuevoProducto: Producto) {
    this.api.post<Producto>('producto/', nuevoProducto).subscribe((respuesta) => {
      this.productos.push(respuesta); 
    });
  }
  
  actualizarProducto(productoActualizado: Producto) {
    this.confirmationService.confirm({
      message: 'No podrás recuperar el producto una vez eliminado',
      header: '¿Estás seguro?',
      icon: 'pi pi-info-circle',
      accept: () => {
          this.messageService.add({ severity: 'succes', summary: 'Producto eliminado', detail: 'El producto se eliminó correctamente' });

          this.api.put<Producto>(`producto/${productoActualizado.id}`, productoActualizado).subscribe(() => {
            const index = this.productos.findIndex((p) => p.id === productoActualizado.id);
            if (index !== -1) {
              this.productos[index] = productoActualizado;
            }
          });
      },
      reject: (type: ConfirmEventType) => {
        switch (type) {
            case ConfirmEventType.REJECT:
                this.messageService.add({ severity: 'info', summary: 'Eliminación cancelada', detail: 'No se eliminó el producto' });
                break;
            case ConfirmEventType.CANCEL:
                this.messageService.add({ severity: 'info', summary: 'Eliminación cancelada', detail: 'No se eliminó el producto' });
                break;
        }
      }
    });    
  }


}
