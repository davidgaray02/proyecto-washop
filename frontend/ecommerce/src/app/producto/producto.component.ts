import { Component, OnInit } from '@angular/core';

import { Producto } from 'src/models/producto.model'; 
import { Categoria } from 'src/models/categoria.model'; 
import { Proveedor } from 'src/models/proveedor.model'; 
import { Negocio } from 'src/models/negocio.model'; 

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

  categorias: Categoria[];
  categoriaSeleccionada: Categoria;
  proveedores: Proveedor[];
  proveedorSeleccionado: Proveedor;
  negocios: Negocio[];
  negocioSeleccionado: Negocio;

  constructor(private api:ApiServicio, private confirmationService: ConfirmationService, private messageService: MessageService){}

  ngOnInit() {
    this.obtenerProductos();

    this.obtenerCategorias();
    this.obtenerProveedores()
    this.obtenerNegocios();
  }

  showCreateBox() {
    this.esNuevoProducto = true;
    this.nuevoProducto = new Producto();
    this.visible = true;

    this.categoriaSeleccionada = new Categoria();
    this.proveedorSeleccionado = new Proveedor();
    this.negocioSeleccionado = new Negocio();
  }

  showEditBox(producto: Producto) {
    this.esNuevoProducto = false;
    this.nuevoProducto = producto;
    this.visible = true;

    this.categoriaSeleccionada = this.categorias.find(categoria => categoria.id === producto.categoria_fk) || this.categorias[0];
  }

  grabarProducto() {
    if (this.esNuevoProducto) {
      this.nuevoProducto.categoria_fk = this.categoriaSeleccionada.id;
      this.nuevoProducto.categoria_nombre = this.categoriaSeleccionada.nombre;
      this.nuevoProducto.proveedor_fk = this.proveedorSeleccionado.id;
      this.nuevoProducto.proveedor_nombre = this.proveedorSeleccionado.nombre;
      this.nuevoProducto.negocio_fk = this.negocioSeleccionado.id;
      this.nuevoProducto.negocio_nombre = this.negocioSeleccionado.nombre;

      this.api.post<Producto>('producto/', this.nuevoProducto).subscribe((respuesta) => {
        this.productos.push(respuesta); 
        this.obtenerProductos();
      });
    } else {
      this.nuevoProducto.categoria_fk = this.categoriaSeleccionada.id;
      this.nuevoProducto.categoria_nombre = this.categoriaSeleccionada.nombre;
      this.nuevoProducto.proveedor_fk = this.proveedorSeleccionado.id;
      this.nuevoProducto.proveedor_nombre = this.proveedorSeleccionado.nombre;
      this.nuevoProducto.negocio_fk = this.negocioSeleccionado.id;
      this.nuevoProducto.negocio_nombre = this.negocioSeleccionado.nombre;

      this.api.put<Producto>(`producto/${this.nuevoProducto.id}`, this.nuevoProducto).subscribe(() => {
        this.obtenerProductos();
      });
    }
    this.visible = false;
  }

  obtenerProductos() {
    this.api.get<Producto[]>('producto').subscribe((respuesta) => {
      this.productos = respuesta; 
    });
  }

  crearProducto(nuevoProducto: Producto) {
    this.api.post<Producto>('producto/', nuevoProducto).subscribe((respuesta) => {
      this.obtenerProductos()
    });
  }
  
  eliminarProducto(productoId: number) {
    this.confirmationService.confirm({
      message: 'No podrás recuperar el producto una vez eliminado',
      header: '¿Estás seguro?',
      icon: 'pi pi-info-circle',
      acceptLabel: 'Sí',
      rejectLabel: 'No',
      acceptButtonStyleClass: 'p-button-danger', 
      rejectButtonStyleClass: 'p-button-secondary',
      acceptIcon: '',
      rejectIcon: '',
      accept: () => {
          this.messageService.add({ severity: 'success', summary: 'Producto eliminado', detail: 'El producto se eliminó correctamente' });

          this.api.delete<void>(`producto/${productoId}`).subscribe(() => {
            this.obtenerProductos()
          });

      },
      reject: (type: ConfirmEventType) => {
        switch (type) {
            case ConfirmEventType.REJECT:
                this.messageService.add({ severity: 'info', summary: 'Eliminación cancelada', detail: 'No se eliminó el producto' });
                break;
            case ConfirmEventType.CANCEL:
                break;
        }
      }
    });    
  }

  obtenerCategorias() {
    this.api.get<Categoria[]>('categoria').subscribe((respuesta) => {
      this.categorias = respuesta; 
      this.categoriaSeleccionada = this.categorias[0]
    });
  }

  obtenerProveedores() {
    this.api.get<Proveedor[]>('proveedor').subscribe((respuesta) => {
      this.proveedores = respuesta; 
      this.proveedorSeleccionado = this.proveedores[0]
    });
  }

  obtenerNegocios() {
    this.api.get<Negocio[]>('negocio').subscribe((respuesta) => {
      this.negocios = respuesta; 
      this.negocioSeleccionado = this.negocios[0]
    });
  }
}
